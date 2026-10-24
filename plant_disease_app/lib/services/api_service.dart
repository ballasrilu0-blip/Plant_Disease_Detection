import 'dart:async';
import 'dart:convert';
import 'package:http/http.dart' as http;
import 'package:image_picker/image_picker.dart';
import '../models/disease_result.dart';

class ApiService {
  // Configurable base URL
  // Defaults to 127.0.0.1:5000 (works on Web, Desktop, and physical Android via 'adb reverse tcp:5000 tcp:5000')
  // For Wi-Fi connection from physical phone: http://10.46.83.116:5000
  // For Android emulator without adb reverse: http://10.0.2.2:5000
  static String baseUrl = 'http://127.0.0.1:5000';

  /// Check server health
  static Future<Map<String, dynamic>> checkHealth([String? testUrl]) async {
    final target = testUrl ?? baseUrl;
    try {
      final url = Uri.parse('$target/api/health');
      final response = await http.get(url).timeout(const Duration(seconds: 5));
      if (response.statusCode == 200) {
        return jsonDecode(response.body) as Map<String, dynamic>;
      } else {
        throw Exception('Server returned status ${response.statusCode}');
      }
    } catch (e) {
      throw Exception('Could not reach backend at $target ($e)');
    }
  }

  /// Upload image and get diagnosis prediction with optional crop filter
  static Future<DiseaseResult> predictImage(XFile imageFile, {String? crop}) async {
    try {
      final url = Uri.parse('$baseUrl/api/predict');
      final request = http.MultipartRequest('POST', url);

      if (crop != null && crop.isNotEmpty && crop != 'Auto-Detect') {
        request.fields['crop'] = crop;
      }

      // Read image bytes - works cross-platform (Web, Android, iOS, Windows)
      final bytes = await imageFile.readAsBytes();
      final multipartFile = http.MultipartFile.fromBytes(
        'image',
        bytes,
        filename: imageFile.name.isNotEmpty ? imageFile.name : 'leaf_upload.jpg',
      );

      request.files.add(multipartFile);

      // Send request with 15s timeout
      final streamedResponse = await request.send().timeout(const Duration(seconds: 15));
      final responseBody = await streamedResponse.stream.bytesToString();

      if (streamedResponse.statusCode == 200) {
        final decoded = jsonDecode(responseBody) as Map<String, dynamic>;
        if (decoded['status'] == 'success' && decoded['prediction'] != null) {
          return DiseaseResult.fromJson(decoded['prediction']);
        } else {
          final msg = decoded['message'] ?? 'Unknown prediction failure';
          throw Exception(msg);
        }
      } else if (streamedResponse.statusCode == 422) {
        // Gatekeeper rejected non-plant image (human, clothing, charger, etc.)
        try {
          final decoded = jsonDecode(responseBody) as Map<String, dynamic>;
          final msg = decoded['message'] ?? 'This does not appear to be a plant leaf.';
          throw Exception(msg);
        } catch (e) {
          if (e is Exception && !e.toString().contains('FormatException')) {
            rethrow;
          }
          throw Exception('The image does not appear to be a plant leaf. Please capture a clear photo of an infected leaf.');
        }
      } else {
        try {
          final errorJson = jsonDecode(responseBody);
          throw Exception(errorJson['message'] ?? 'Server error (${streamedResponse.statusCode})');
        } catch (_) {
          throw Exception('Server returned error code ${streamedResponse.statusCode}');
        }
      }
    } on TimeoutException {
      throw Exception(
        'Connection timed out while connecting to:\n$baseUrl\n\n'
        '• If phone is connected via USB: Tap Settings (top right) and select "USB / Localhost (127.0.0.1:5000)".\n'
        '• If using Wi-Fi: Make sure PC and phone are on the same Wi-Fi, then select "Wi-Fi (10.46.83.116:5000)".\n'
        '• Ensure "python web_app/app.py" is running on your PC.',
      );
    } catch (e) {
      final str = e.toString().toLowerCase();
      if (str.contains('socketexception') ||
          str.contains('failed to connect') ||
          str.contains('connection refused') ||
          str.contains('network is unreachable')) {
        throw Exception(
          'Cannot reach backend server at:\n$baseUrl\n\n'
          '• If phone is connected via USB: Tap Settings (top right) and select "USB / Localhost (127.0.0.1:5000)".\n'
          '• If using Wi-Fi: Tap Settings and select "Wi-Fi (10.46.83.116:5000)".\n'
          '• Ensure "python web_app/app.py" is running on your PC.',
        );
      }
      rethrow;
    }
  }
}
