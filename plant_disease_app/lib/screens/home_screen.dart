import 'dart:typed_data';
import 'package:flutter/material.dart';
import 'package:image_picker/image_picker.dart';
import '../models/disease_result.dart';
import '../services/api_service.dart';
import 'result_screen.dart';

class HomeScreen extends StatefulWidget {
  const HomeScreen({super.key});

  @override
  State<HomeScreen> createState() => _HomeScreenState();
}

class _HomeScreenState extends State<HomeScreen> {
  final ImagePicker _picker = ImagePicker();
  XFile? _selectedImage;
  Uint8List? _imageBytes;
  bool _isLoading = false;
  String? _errorMessage;

  static const List<String> supportedCrops = [
    'Auto-Detect',
    'Apple',
    'Banana',
    'Bell Pepper',
    'Citrus',
    'Corn',
    'Grape',
    'Guava',
    'Mango',
    'Papaya',
    'Potato',
    'Tomato',
  ];
  String _selectedCrop = 'Auto-Detect';

  Future<void> _pickImage(ImageSource source) async {
    setState(() {
      _errorMessage = null;
    });

    try {
      final picked = await _picker.pickImage(
        source: source,
        maxWidth: 1024,
        maxHeight: 1024,
        imageQuality: 85,
      );

      if (picked != null) {
        final bytes = await picked.readAsBytes();
        setState(() {
          _selectedImage = picked;
          _imageBytes = bytes;
          _errorMessage = null;
        });
      }
    } catch (e) {
      setState(() {
        _errorMessage = 'Failed to pick image: $e';
      });
    }
  }

  void _clearImage() {
    setState(() {
      _selectedImage = null;
      _imageBytes = null;
      _errorMessage = null;
    });
  }

  Future<void> _diagnoseLeaf() async {
    if (_selectedImage == null) return;

    setState(() {
      _isLoading = true;
      _errorMessage = null;
    });

    try {
      final DiseaseResult result = await ApiService.predictImage(
        _selectedImage!,
        crop: _selectedCrop,
      );

      if (!mounted) return;

      Navigator.push(
        context,
        MaterialPageRoute(
          builder: (context) => ResultScreen(
            result: result,
            imageBytes: _imageBytes,
          ),
        ),
      );
    } catch (e) {
      setState(() {
        _errorMessage = e.toString().replaceFirst('Exception: ', '');
      });
    } finally {
      if (mounted) {
        setState(() {
          _isLoading = false;
        });
      }
    }
  }

  void _showServerSettings() {
    final controller = TextEditingController(text: ApiService.baseUrl);
    String? statusMessage;
    bool isTesting = false;

    showDialog(
      context: context,
      builder: (context) => StatefulBuilder(
        builder: (context, setDialogState) => AlertDialog(
          shape: RoundedRectangleBorder(borderRadius: BorderRadius.circular(16)),
          title: const Row(
            children: [
              Icon(Icons.dns_outlined, color: Color(0xFF2E7D32)),
              SizedBox(width: 8),
              Text('Server Settings', style: TextStyle(fontSize: 18)),
            ],
          ),
          content: Column(
            mainAxisSize: MainAxisSize.min,
            crossAxisAlignment: CrossAxisAlignment.start,
            children: [
              const Text(
                'Configure the Flask backend API address:',
                style: TextStyle(fontSize: 13, color: Colors.black87),
              ),
              const SizedBox(height: 10),
              TextField(
                controller: controller,
                decoration: const InputDecoration(
                  labelText: 'Backend URL',
                  hintText: 'http://127.0.0.1:5000',
                  border: OutlineInputBorder(),
                  prefixIcon: Icon(Icons.link),
                  contentPadding: EdgeInsets.symmetric(horizontal: 12, vertical: 10),
                ),
              ),
              const SizedBox(height: 10),
              const Text(
                'Quick Presets (tap to select):',
                style: TextStyle(fontSize: 12, fontWeight: FontWeight.bold, color: Colors.black54),
              ),
              const SizedBox(height: 6),
              Wrap(
                spacing: 6,
                runSpacing: 6,
                children: [
                  ActionChip(
                    avatar: const Icon(Icons.usb, size: 16),
                    label: const Text('USB Cable (127.0.0.1:5000)', style: TextStyle(fontSize: 11)),
                    onPressed: () {
                      setDialogState(() {
                        controller.text = 'http://127.0.0.1:5000';
                      });
                    },
                  ),
                  ActionChip(
                    avatar: const Icon(Icons.wifi, size: 16),
                    label: const Text('Wi-Fi (10.46.83.116:5000)', style: TextStyle(fontSize: 11)),
                    onPressed: () {
                      setDialogState(() {
                        controller.text = 'http://10.46.83.116:5000';
                      });
                    },
                  ),
                  ActionChip(
                    avatar: const Icon(Icons.phone_android, size: 16),
                    label: const Text('Emulator (10.0.2.2:5000)', style: TextStyle(fontSize: 11)),
                    onPressed: () {
                      setDialogState(() {
                        controller.text = 'http://10.0.2.2:5000';
                      });
                    },
                  ),
                ],
              ),
              if (statusMessage != null) ...[
                const SizedBox(height: 12),
                Text(
                  statusMessage!,
                  style: TextStyle(
                    fontSize: 12,
                    fontWeight: FontWeight.bold,
                    color: statusMessage!.contains('Online') ? Colors.green.shade700 : Colors.red.shade700,
                  ),
                ),
              ],
            ],
          ),
          actions: [
            TextButton(
              onPressed: isTesting
                  ? null
                  : () async {
                      setDialogState(() {
                        isTesting = true;
                        statusMessage = 'Testing connection...';
                      });
                      final original = ApiService.baseUrl;
                      ApiService.baseUrl = controller.text.trim();
                      try {
                        final health = await ApiService.checkHealth();
                        setDialogState(() {
                          isTesting = false;
                          statusMessage = 'Online: ${health['model']} (${health['classes_count']} classes)';
                        });
                      } catch (err) {
                        ApiService.baseUrl = original;
                        setDialogState(() {
                          isTesting = false;
                          statusMessage = 'Connection failed: $err';
                        });
                      }
                    },
              child: isTesting
                  ? const SizedBox(width: 16, height: 16, child: CircularProgressIndicator(strokeWidth: 2))
                  : const Text('Test Connection'),
            ),
            ElevatedButton(
              onPressed: () {
                ApiService.baseUrl = controller.text.trim();
                Navigator.pop(context);
                ScaffoldMessenger.of(context).showSnackBar(
                  SnackBar(content: Text('Server URL set to: ${ApiService.baseUrl}')),
                );
              },
              child: const Text('Save'),
            ),
          ],
        ),
      ),
    );
  }

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        title: const Row(
          children: [
            Icon(Icons.eco_rounded, color: Colors.white),
            SizedBox(width: 8),
            Text('Plant Disease AI', style: TextStyle(fontWeight: FontWeight.bold)),
          ],
        ),
        actions: [
          IconButton(
            tooltip: 'Server Settings',
            icon: const Icon(Icons.settings_outlined),
            onPressed: _showServerSettings,
          ),
        ],
      ),
      body: SingleChildScrollView(
        padding: const EdgeInsets.all(16.0),
        child: Column(
          crossAxisAlignment: CrossAxisAlignment.stretch,
          children: [
            // Welcome Card
            _buildHeroCard(),
            const SizedBox(height: 18),

            // Image Picker / Preview Container
            _buildImageContainer(),
            const SizedBox(height: 18),

            // Error / Gatekeeper Notice (if any)
            if (_errorMessage != null) ...[
              Builder(
                builder: (context) {
                  final isGatekeeper = _errorMessage!.toLowerCase().contains('human') ||
                      _errorMessage!.toLowerCase().contains('clothing') ||
                      _errorMessage!.toLowerCase().contains('fabric') ||
                      _errorMessage!.toLowerCase().contains('electronics') ||
                      _errorMessage!.toLowerCase().contains('charger') ||
                      _errorMessage!.toLowerCase().contains('not appear') ||
                      _errorMessage!.toLowerCase().contains('plant leaf') ||
                      _errorMessage!.toLowerCase().contains('low confidence');

                  final bgColor = isGatekeeper ? const Color(0xFFFFF8E1) : Colors.red.shade50;
                  final borderColor = isGatekeeper ? const Color(0xFFFFE082) : Colors.red.shade200;
                  final textColor = isGatekeeper ? const Color(0xFFE65100) : Colors.red.shade900;
                  final iconColor = isGatekeeper ? const Color(0xFFF57C00) : Colors.red.shade700;
                  final icon = isGatekeeper ? Icons.shield_outlined : Icons.error_outline;

                  return Container(
                    padding: const EdgeInsets.all(14),
                    decoration: BoxDecoration(
                      color: bgColor,
                      borderRadius: BorderRadius.circular(14),
                      border: Border.all(color: borderColor),
                    ),
                    child: Column(
                      crossAxisAlignment: CrossAxisAlignment.start,
                      children: [
                        Row(
                          crossAxisAlignment: CrossAxisAlignment.start,
                          children: [
                            Icon(icon, color: iconColor, size: 22),
                            const SizedBox(width: 10),
                            Expanded(
                              child: Column(
                                crossAxisAlignment: CrossAxisAlignment.start,
                                children: [
                                  if (isGatekeeper) ...[
                                    Text(
                                      'Gatekeeper Notice',
                                      style: TextStyle(color: textColor, fontWeight: FontWeight.bold, fontSize: 13),
                                    ),
                                    const SizedBox(height: 3),
                                  ],
                                  Text(
                                    _errorMessage!,
                                    style: TextStyle(color: textColor, fontSize: 13, height: 1.35),
                                  ),
                                ],
                              ),
                            ),
                          ],
                        ),
                        const SizedBox(height: 10),
                        Align(
                          alignment: Alignment.centerRight,
                          child: isGatekeeper
                              ? TextButton.icon(
                                  onPressed: _clearImage,
                                  icon: const Icon(Icons.refresh, size: 16),
                                  label: const Text('Capture Plant Leaf', style: TextStyle(fontWeight: FontWeight.bold, fontSize: 13)),
                                  style: TextButton.styleFrom(
                                    foregroundColor: textColor,
                                    backgroundColor: const Color(0xFFFFECB3),
                                    padding: const EdgeInsets.symmetric(horizontal: 12, vertical: 6),
                                  ),
                                )
                              : TextButton.icon(
                                  onPressed: _showServerSettings,
                                  icon: const Icon(Icons.settings, size: 16),
                                  label: const Text('Change Server Address', style: TextStyle(fontWeight: FontWeight.bold, fontSize: 13)),
                                  style: TextButton.styleFrom(
                                    foregroundColor: Colors.red.shade900,
                                    backgroundColor: Colors.red.shade100,
                                    padding: const EdgeInsets.symmetric(horizontal: 12, vertical: 6),
                                  ),
                                ),
                        ),
                      ],
                    ),
                  );
                },
              ),
              const SizedBox(height: 18),
            ],

            // Action Buttons
            if (_imageBytes == null) ...[
              Row(
                children: [
                  Expanded(
                    child: ElevatedButton.icon(
                      onPressed: () => _pickImage(ImageSource.camera),
                      icon: const Icon(Icons.camera_alt_rounded),
                      label: const Text('Take Photo'),
                      style: ElevatedButton.styleFrom(
                        padding: const EdgeInsets.symmetric(vertical: 14),
                        shape: RoundedRectangleBorder(borderRadius: BorderRadius.circular(12)),
                      ),
                    ),
                  ),
                  const SizedBox(width: 12),
                  Expanded(
                    child: OutlinedButton.icon(
                      onPressed: () => _pickImage(ImageSource.gallery),
                      icon: const Icon(Icons.photo_library_rounded),
                      label: const Text('Gallery'),
                      style: OutlinedButton.styleFrom(
                        padding: const EdgeInsets.symmetric(vertical: 14),
                        shape: RoundedRectangleBorder(borderRadius: BorderRadius.circular(12)),
                      ),
                    ),
                  ),
                ],
              ),
            ] else ...[
              // Optional Crop Target Selector
              Container(
                padding: const EdgeInsets.symmetric(horizontal: 14, vertical: 4),
                decoration: BoxDecoration(
                  color: Colors.green.shade50.withValues(alpha: 0.6),
                  borderRadius: BorderRadius.circular(12),
                  border: Border.all(color: Colors.green.shade200),
                ),
                child: Row(
                  children: [
                    const Icon(Icons.eco_rounded, color: Color(0xFF2E7D32), size: 20),
                    const SizedBox(width: 10),
                    const Text(
                      'Crop / Plant:',
                      style: TextStyle(fontSize: 13, fontWeight: FontWeight.bold, color: Color(0xFF1B5E20)),
                    ),
                    const SizedBox(width: 8),
                    Expanded(
                      child: DropdownButtonHideUnderline(
                        child: DropdownButton<String>(
                          value: _selectedCrop,
                          isExpanded: true,
                          icon: const Icon(Icons.arrow_drop_down, color: Color(0xFF2E7D32)),
                          items: supportedCrops.map((crop) {
                            return DropdownMenuItem<String>(
                              value: crop,
                              child: Text(
                                crop == 'Auto-Detect' ? '🌿 Auto-Detect (All Crops)' : crop,
                                style: TextStyle(
                                  fontSize: 13,
                                  color: crop == 'Auto-Detect' ? Colors.black87 : const Color(0xFF1B5E20),
                                  fontWeight: crop == 'Auto-Detect' ? FontWeight.normal : FontWeight.w600,
                                ),
                              ),
                            );
                          }).toList(),
                          onChanged: (val) {
                            if (val != null) {
                              setState(() {
                                _selectedCrop = val;
                              });
                            }
                          },
                        ),
                      ),
                    ),
                  ],
                ),
              ),
              const SizedBox(height: 12),

              Row(
                children: [
                  Expanded(
                    flex: 2,
                    child: ElevatedButton.icon(
                      onPressed: _isLoading ? null : _diagnoseLeaf,
                      icon: _isLoading
                          ? const SizedBox(
                              width: 20,
                              height: 20,
                              child: CircularProgressIndicator(strokeWidth: 2, color: Colors.white),
                            )
                          : const Icon(Icons.search_rounded),
                      label: Text(
                        _isLoading ? 'Analyzing...' : 'Diagnose Disease',
                        style: const TextStyle(fontSize: 16, fontWeight: FontWeight.bold),
                      ),
                      style: ElevatedButton.styleFrom(
                        backgroundColor: const Color(0xFF2E7D32),
                        foregroundColor: Colors.white,
                        padding: const EdgeInsets.symmetric(vertical: 14),
                        shape: RoundedRectangleBorder(borderRadius: BorderRadius.circular(12)),
                      ),
                    ),
                  ),
                  const SizedBox(width: 10),
                  IconButton.filledTonal(
                    onPressed: _isLoading ? null : _clearImage,
                    icon: const Icon(Icons.refresh_rounded),
                    tooltip: 'Select Another Image',
                  ),
                ],
              ),
            ],
            const SizedBox(height: 24),

            // Supported Crops Section
            _buildSupportedCropsCard(),
            const SizedBox(height: 16),

            // Tips Section
            _buildTipsCard(),
          ],
        ),
      ),
    );
  }

  Widget _buildHeroCard() {
    return Container(
      decoration: BoxDecoration(
        gradient: const LinearGradient(
          colors: [Color(0xFF1B5E20), Color(0xFF388E3C)],
          begin: Alignment.topLeft,
          end: Alignment.bottomRight,
        ),
        borderRadius: BorderRadius.circular(16),
        boxShadow: const [
          BoxShadow(color: Colors.black12, blurRadius: 8, offset: Offset(0, 3)),
        ],
      ),
      padding: const EdgeInsets.all(20),
      child: const Column(
        crossAxisAlignment: CrossAxisAlignment.start,
        children: [
          Row(
            children: [
              Icon(Icons.local_florist, color: Colors.white, size: 24),
              SizedBox(width: 8),
              Text(
                'Instant Crop Diagnosis',
                style: TextStyle(color: Colors.white, fontSize: 18, fontWeight: FontWeight.bold),
              ),
            ],
          ),
          SizedBox(height: 8),
          Text(
            'Capture or upload a clear photo of an infected or healthy leaf to get instant AI disease diagnosis and expert treatment recommendations.',
            style: TextStyle(color: Colors.white70, fontSize: 13.5, height: 1.4),
          ),
        ],
      ),
    );
  }

  Widget _buildImageContainer() {
    if (_imageBytes != null) {
      return Container(
        height: 260,
        decoration: BoxDecoration(
          borderRadius: BorderRadius.circular(16),
          border: Border.all(color: Colors.grey.shade300),
          boxShadow: const [
            BoxShadow(color: Colors.black12, blurRadius: 6, offset: Offset(0, 2)),
          ],
        ),
        child: ClipRRect(
          borderRadius: BorderRadius.circular(16),
          child: Stack(
            fit: StackFit.expand,
            children: [
              Image.memory(
                _imageBytes!,
                fit: BoxFit.cover,
              ),
              Positioned(
                top: 8,
                right: 8,
                child: CircleAvatar(
                  backgroundColor: Colors.black54,
                  radius: 18,
                  child: IconButton(
                    icon: const Icon(Icons.close, color: Colors.white, size: 18),
                    onPressed: _clearImage,
                  ),
                ),
              ),
            ],
          ),
        ),
      );
    }

    return GestureDetector(
      onTap: () => _pickImage(ImageSource.gallery),
      child: Container(
        height: 220,
        decoration: BoxDecoration(
          color: Colors.grey.shade50,
          borderRadius: BorderRadius.circular(16),
          border: Border.all(color: Colors.grey.shade400, style: BorderStyle.solid),
        ),
        child: Column(
          mainAxisAlignment: MainAxisAlignment.center,
          children: [
            CircleAvatar(
              radius: 36,
              backgroundColor: Colors.green.shade50,
              child: Icon(Icons.add_photo_alternate_rounded, size: 36, color: Colors.green.shade700),
            ),
            const SizedBox(height: 12),
            const Text(
              'Select a leaf image to diagnose',
              style: TextStyle(fontSize: 15, fontWeight: FontWeight.bold, color: Colors.black87),
            ),
            const SizedBox(height: 4),
            Text(
              'Supports JPG, PNG, WEBP (62 Classes)',
              style: TextStyle(fontSize: 12, color: Colors.grey.shade600),
            ),
          ],
        ),
      ),
    );
  }

  Widget _buildSupportedCropsCard() {
    final cropsList = [
      '🍏 Apple', '🍌 Banana', '🫑 Bell Pepper', '🍊 Citrus',
      '🌽 Corn', '🍇 Grape', '🍈 Guava', '🥭 Mango',
      '🍈 Papaya', '🥔 Potato', '🍅 Tomato',
    ];

    return Card(
      elevation: 0,
      color: Colors.blueGrey.shade50.withValues(alpha: 0.6),
      shape: RoundedRectangleBorder(
        borderRadius: BorderRadius.circular(16),
        side: BorderSide(color: Colors.blueGrey.shade200),
      ),
      child: Padding(
        padding: const EdgeInsets.all(16.0),
        child: Column(
          crossAxisAlignment: CrossAxisAlignment.start,
          children: [
            Row(
              children: [
                Icon(Icons.grass_rounded, color: Colors.blueGrey.shade800, size: 20),
                const SizedBox(width: 8),
                Text(
                  'Supported Crops (11 Plants, 62 Diseases)',
                  style: TextStyle(
                    fontWeight: FontWeight.bold,
                    fontSize: 14,
                    color: Colors.blueGrey.shade900,
                  ),
                ),
              ],
            ),
            const SizedBox(height: 10),
            Wrap(
              spacing: 6,
              runSpacing: 6,
              children: cropsList.map((c) {
                return Chip(
                  label: Text(c, style: const TextStyle(fontSize: 11.5)),
                  padding: const EdgeInsets.symmetric(horizontal: 4, vertical: 0),
                  backgroundColor: Colors.white,
                  side: BorderSide(color: Colors.blueGrey.shade100),
                  materialTapTargetSize: MaterialTapTargetSize.shrinkWrap,
                );
              }).toList(),
            ),
            const SizedBox(height: 10),
            Text(
              'ℹ️ Important: This AI is trained on these 11 crops. Unsupported species (like Blueberry, Strawberry, Rice, or Rose) will map to the closest visual symptom among the 11 supported plants.',
              style: TextStyle(fontSize: 12, color: Colors.blueGrey.shade700, height: 1.35),
            ),
          ],
        ),
      ),
    );
  }

  Widget _buildTipsCard() {
    return Card(
      elevation: 0,
      color: Colors.green.shade50.withValues(alpha: 0.5),
      shape: RoundedRectangleBorder(
        borderRadius: BorderRadius.circular(16),
        side: BorderSide(color: Colors.green.shade100),
      ),
      child: const Padding(
        padding: EdgeInsets.all(16.0),
        child: Column(
          crossAxisAlignment: CrossAxisAlignment.start,
          children: [
            Row(
              children: [
                Icon(Icons.lightbulb_outline, color: Color(0xFF2E7D32), size: 20),
                SizedBox(width: 8),
                Text(
                  'Tips for Accurate Diagnosis',
                  style: TextStyle(fontWeight: FontWeight.bold, fontSize: 14, color: Color(0xFF1B5E20)),
                ),
              ],
            ),
            SizedBox(height: 10),
            Text('• Place leaf flat against a neutral background if possible', style: TextStyle(fontSize: 12.5, height: 1.4)),
            Text('• Ensure sharp focus on visible disease spots or discoloration', style: TextStyle(fontSize: 12.5, height: 1.4)),
            Text('• Avoid extreme glare, shadows, or blurry camera motion', style: TextStyle(fontSize: 12.5, height: 1.4)),
          ],
        ),
      ),
    );
  }
}
