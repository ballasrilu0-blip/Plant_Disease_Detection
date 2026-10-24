import 'dart:typed_data';
import 'package:flutter/material.dart';
import '../models/disease_result.dart';

class ResultScreen extends StatelessWidget {
  final DiseaseResult result;
  final Uint8List? imageBytes;

  const ResultScreen({
    super.key,
    required this.result,
    this.imageBytes,
  });

  @override
  Widget build(BuildContext context) {
    final isHealthy = result.isHealthy;
    final primaryColor = isHealthy ? Colors.teal : Colors.deepOrange;

    return Scaffold(
      appBar: AppBar(
        title: const Text('Diagnosis Report'),
        backgroundColor: isHealthy ? const Color(0xFF1B5E20) : const Color(0xFFBF360C),
        foregroundColor: Colors.white,
        elevation: 0,
      ),
      body: SingleChildScrollView(
        child: Column(
          crossAxisAlignment: CrossAxisAlignment.stretch,
          children: [
            // Header Image and Quick Summary
            _buildHeader(context, isHealthy, primaryColor),

            Padding(
              padding: const EdgeInsets.symmetric(horizontal: 16.0, vertical: 12.0),
              child: Column(
                crossAxisAlignment: CrossAxisAlignment.stretch,
                children: [
                  // Confidence Meter Card
                  _buildConfidenceCard(context, primaryColor),
                  const SizedBox(height: 16),

                  // Low Confidence Warning (if confidence < 45%)
                  if (result.confidence < 45.0) ...[
                    _buildLowConfidenceWarning(context),
                    const SizedBox(height: 16),
                  ],

                  // Immediate Action (if not healthy)
                  if (!isHealthy && result.immediateAction.isNotEmpty) ...[
                    _buildImmediateActionCard(context),
                    const SizedBox(height: 16),
                  ],

                  // Symptoms Section
                  if (result.symptoms.isNotEmpty) ...[
                    _buildSectionCard(
                      title: 'Observable Symptoms',
                      icon: Icons.biotech_outlined,
                      accentColor: Colors.blue.shade700,
                      content: Column(
                        crossAxisAlignment: CrossAxisAlignment.start,
                        children: result.symptoms.map((s) => _buildBulletPoint(s)).toList(),
                      ),
                    ),
                    const SizedBox(height: 16),
                  ],

                  // Pathogen & Causes
                  if (result.cause.isNotEmpty || result.pathogen.isNotEmpty) ...[
                    _buildSectionCard(
                      title: 'Cause & Pathogen',
                      icon: Icons.coronavirus_outlined,
                      accentColor: Colors.purple.shade700,
                      content: Column(
                        crossAxisAlignment: CrossAxisAlignment.start,
                        children: [
                          if (result.pathogen.isNotEmpty) ...[
                            Text(
                              'Pathogen: ${result.pathogen}',
                              style: const TextStyle(fontWeight: FontWeight.bold, fontSize: 14),
                            ),
                            const SizedBox(height: 6),
                          ],
                          if (result.cause.isNotEmpty)
                            Text(
                              result.cause,
                              style: const TextStyle(fontSize: 14, height: 1.4),
                            ),
                        ],
                      ),
                    ),
                    const SizedBox(height: 16),
                  ],

                  // Favorable Conditions
                  if (result.favorableConditions.isNotEmpty) ...[
                    _buildSectionCard(
                      title: 'Favorable Conditions',
                      icon: Icons.cloud_outlined,
                      accentColor: Colors.amber.shade800,
                      content: Column(
                        crossAxisAlignment: CrossAxisAlignment.start,
                        children: result.favorableConditions.map((c) => _buildBulletPoint(c)).toList(),
                      ),
                    ),
                    const SizedBox(height: 16),
                  ],

                  // Remedies & Treatments
                  if (!isHealthy && (result.biologicalControl.isNotEmpty || result.chemicalControl.isNotEmpty)) ...[
                    _buildSectionCard(
                      title: 'Treatment & Remedies',
                      icon: Icons.medical_services_outlined,
                      accentColor: Colors.green.shade700,
                      content: Column(
                        crossAxisAlignment: CrossAxisAlignment.start,
                        children: [
                          if (result.biologicalControl.isNotEmpty) ...[
                            const Text(
                              'Organic / Biological Control:',
                              style: TextStyle(fontWeight: FontWeight.bold, fontSize: 14),
                            ),
                            const SizedBox(height: 6),
                            ...result.biologicalControl.map((b) => _buildBulletPoint(b)),
                            const SizedBox(height: 12),
                          ],
                          if (result.chemicalControl.isNotEmpty) ...[
                            const Text(
                              'Chemical Treatment:',
                              style: TextStyle(fontWeight: FontWeight.bold, fontSize: 14),
                            ),
                            const SizedBox(height: 6),
                            Text(
                              result.chemicalControl,
                              style: const TextStyle(fontSize: 14, height: 1.4),
                            ),
                          ],
                        ],
                      ),
                    ),
                    const SizedBox(height: 16),
                  ],

                  // Prevention
                  if (result.prevention.isNotEmpty) ...[
                    _buildSectionCard(
                      title: 'Prevention & Best Practices',
                      icon: Icons.shield_outlined,
                      accentColor: Colors.teal.shade700,
                      content: Column(
                        crossAxisAlignment: CrossAxisAlignment.start,
                        children: result.prevention.map((p) => _buildBulletPoint(p)).toList(),
                      ),
                    ),
                    const SizedBox(height: 16),
                  ],

                  // Alternative Top Predictions
                  if (result.topPredictions.isNotEmpty) ...[
                    _buildTopPredictionsCard(context),
                    const SizedBox(height: 24),
                  ],
                ],
              ),
            ),
          ],
        ),
      ),
    );
  }

  Widget _buildHeader(BuildContext context, bool isHealthy, Color primaryColor) {
    return Container(
      decoration: BoxDecoration(
        color: isHealthy ? const Color(0xFF1B5E20) : const Color(0xFFBF360C),
        borderRadius: const BorderRadius.only(
          bottomLeft: Radius.circular(24),
          bottomRight: Radius.circular(24),
        ),
      ),
      padding: const EdgeInsets.fromLTRB(20, 10, 20, 24),
      child: Column(
        children: [
          if (imageBytes != null)
            Container(
              height: 180,
              width: double.infinity,
              decoration: BoxDecoration(
                borderRadius: BorderRadius.circular(16),
                boxShadow: const [
                  BoxShadow(color: Colors.black26, blurRadius: 10, offset: Offset(0, 4))
                ],
              ),
              child: ClipRRect(
                borderRadius: BorderRadius.circular(16),
                child: Image.memory(
                  imageBytes!,
                  fit: BoxFit.cover,
                ),
              ),
            ),
          const SizedBox(height: 16),
          // Health status chip
          Container(
            padding: const EdgeInsets.symmetric(horizontal: 14, vertical: 6),
            decoration: BoxDecoration(
              color: Colors.white.withValues(alpha: 0.2),
              borderRadius: BorderRadius.circular(20),
            ),
            child: Row(
              mainAxisSize: MainAxisSize.min,
              children: [
                Icon(
                  isHealthy ? Icons.check_circle : Icons.warning_amber_rounded,
                  color: Colors.white,
                  size: 18,
                ),
                const SizedBox(width: 6),
                Text(
                  isHealthy ? 'HEALTHY PLANT' : 'DISEASE DETECTED (${result.diseaseType})',
                  style: const TextStyle(
                    color: Colors.white,
                    fontWeight: FontWeight.bold,
                    fontSize: 12,
                    letterSpacing: 0.5,
                  ),
                ),
              ],
            ),
          ),
          const SizedBox(height: 10),
          Text(
            result.disease,
            textAlign: TextAlign.center,
            style: const TextStyle(
              color: Colors.white,
              fontSize: 22,
              fontWeight: FontWeight.bold,
            ),
          ),
          const SizedBox(height: 4),
          Text(
            'Host Plant: ${result.plant} • Part: ${result.affectedPart}',
            textAlign: TextAlign.center,
            style: const TextStyle(
              color: Colors.white70,
              fontSize: 14,
            ),
          ),
        ],
      ),
    );
  }

  Widget _buildConfidenceCard(BuildContext context, Color primaryColor) {
    return Card(
      elevation: 2,
      shape: RoundedRectangleBorder(borderRadius: BorderRadius.circular(16)),
      child: Padding(
        padding: const EdgeInsets.all(16.0),
        child: Column(
          children: [
            Row(
              mainAxisAlignment: MainAxisAlignment.spaceBetween,
              children: [
                const Text(
                  'Model Confidence',
                  style: TextStyle(fontSize: 16, fontWeight: FontWeight.bold),
                ),
                Text(
                  '${result.confidence.toStringAsFixed(1)}%',
                  style: TextStyle(
                    fontSize: 18,
                    fontWeight: FontWeight.bold,
                    color: primaryColor,
                  ),
                ),
              ],
            ),
            const SizedBox(height: 10),
            ClipRRect(
              borderRadius: BorderRadius.circular(8),
              child: LinearProgressIndicator(
                value: (result.confidence / 100).clamp(0.0, 1.0),
                minHeight: 10,
                backgroundColor: Colors.grey.shade200,
                color: primaryColor,
              ),
            ),
          ],
        ),
      ),
    );
  }

  Widget _buildLowConfidenceWarning(BuildContext context) {
    final hasSecondCandidate = result.topPredictions.length > 1;
    final secondCandidate = hasSecondCandidate ? result.topPredictions[1] : null;

    return Container(
      padding: const EdgeInsets.all(14),
      decoration: BoxDecoration(
        color: const Color(0xFFFFF3E0),
        borderRadius: BorderRadius.circular(16),
        border: Border.all(color: const Color(0xFFFFB74D), width: 1.2),
      ),
      child: Row(
        crossAxisAlignment: CrossAxisAlignment.start,
        children: [
          const Icon(Icons.warning_amber_rounded, color: Color(0xFFE65100), size: 24),
          const SizedBox(width: 12),
          Expanded(
            child: Column(
              crossAxisAlignment: CrossAxisAlignment.start,
              children: [
                const Text(
                  'Uncertain Diagnosis (Low Confidence)',
                  style: TextStyle(
                    fontWeight: FontWeight.bold,
                    color: Color(0xFFE65100),
                    fontSize: 14,
                  ),
                ),
                const SizedBox(height: 4),
                Text(
                  'The AI is only ${result.confidence.toStringAsFixed(1)}% confident about "${result.disease}". '
                  '${secondCandidate != null ? 'Close alternative: "${secondCandidate.plant} - ${secondCandidate.disease}" (${secondCandidate.confidence.toStringAsFixed(1)}%).' : ''}\n\n'
                  '💡 Tips for an accurate diagnosis:\n'
                  '• Do NOT photograph a computer/phone screen (screen pixel grids confuse the AI).\n'
                  '• Capture a clear, close-up photo of the actual plant leaf in good daylight.\n'
                  '• Keep the infected leaf centered and in focus.',
                  style: const TextStyle(
                    color: Color(0xFFBF360C),
                    fontSize: 12.5,
                    height: 1.4,
                  ),
                ),
              ],
            ),
          ),
        ],
      ),
    );
  }

  Widget _buildImmediateActionCard(BuildContext context) {
    return Container(
      decoration: BoxDecoration(
        color: Colors.red.shade50,
        borderRadius: BorderRadius.circular(16),
        border: Border.all(color: Colors.red.shade200),
      ),
      padding: const EdgeInsets.all(16),
      child: Column(
        crossAxisAlignment: CrossAxisAlignment.start,
        children: [
          Row(
            children: [
              Icon(Icons.bolt, color: Colors.red.shade700),
              const SizedBox(width: 8),
              Text(
                'Immediate Action Required',
                style: TextStyle(
                  color: Colors.red.shade900,
                  fontSize: 16,
                  fontWeight: FontWeight.bold,
                ),
              ),
            ],
          ),
          const SizedBox(height: 10),
          ...result.immediateAction.map(
            (action) => Padding(
              padding: const EdgeInsets.only(bottom: 6.0),
              child: Row(
                crossAxisAlignment: CrossAxisAlignment.start,
                children: [
                  Text('• ', style: TextStyle(color: Colors.red.shade700, fontWeight: FontWeight.bold)),
                  Expanded(
                    child: Text(
                      action,
                      style: TextStyle(color: Colors.red.shade900, fontSize: 13, height: 1.3),
                    ),
                  ),
                ],
              ),
            ),
          ),
        ],
      ),
    );
  }

  Widget _buildSectionCard({
    required String title,
    required IconData icon,
    required Color accentColor,
    required Widget content,
  }) {
    return Card(
      elevation: 1.5,
      shape: RoundedRectangleBorder(borderRadius: BorderRadius.circular(16)),
      child: Padding(
        padding: const EdgeInsets.all(16),
        child: Column(
          crossAxisAlignment: CrossAxisAlignment.start,
          children: [
            Row(
              children: [
                Icon(icon, color: accentColor, size: 22),
                const SizedBox(width: 10),
                Text(
                  title,
                  style: const TextStyle(fontSize: 16, fontWeight: FontWeight.bold),
                ),
              ],
            ),
            const Divider(height: 20),
            content,
          ],
        ),
      ),
    );
  }

  Widget _buildBulletPoint(String text) {
    return Padding(
      padding: const EdgeInsets.only(bottom: 6.0),
      child: Row(
        crossAxisAlignment: CrossAxisAlignment.start,
        children: [
          const Text('• ', style: TextStyle(fontWeight: FontWeight.bold, fontSize: 14)),
          Expanded(
            child: Text(
              text,
              style: const TextStyle(fontSize: 13.5, height: 1.35),
            ),
          ),
        ],
      ),
    );
  }

  Widget _buildTopPredictionsCard(BuildContext context) {
    return Card(
      elevation: 1.5,
      shape: RoundedRectangleBorder(borderRadius: BorderRadius.circular(16)),
      child: Padding(
        padding: const EdgeInsets.all(16),
        child: Column(
          crossAxisAlignment: CrossAxisAlignment.start,
          children: [
            const Row(
              children: [
                Icon(Icons.format_list_bulleted, color: Colors.blueGrey, size: 20),
                SizedBox(width: 8),
                Text(
                  'Differential Candidates (Top 3)',
                  style: TextStyle(fontSize: 15, fontWeight: FontWeight.bold),
                ),
              ],
            ),
            const SizedBox(height: 12),
            ...result.topPredictions.map((pred) {
              return Padding(
                padding: const EdgeInsets.only(bottom: 10.0),
                child: Column(
                  crossAxisAlignment: CrossAxisAlignment.start,
                  children: [
                    Row(
                      mainAxisAlignment: MainAxisAlignment.spaceBetween,
                      children: [
                        Expanded(
                          child: Text(
                            '${pred.plant} - ${pred.disease}',
                            style: const TextStyle(fontSize: 13, fontWeight: FontWeight.w500),
                            overflow: TextOverflow.ellipsis,
                          ),
                        ),
                        Text(
                          '${pred.confidence.toStringAsFixed(1)}%',
                          style: const TextStyle(fontSize: 12, fontWeight: FontWeight.bold),
                        ),
                      ],
                    ),
                    const SizedBox(height: 4),
                    ClipRRect(
                      borderRadius: BorderRadius.circular(4),
                      child: LinearProgressIndicator(
                        value: (pred.confidence / 100).clamp(0.0, 1.0),
                        minHeight: 5,
                        backgroundColor: Colors.grey.shade200,
                        color: Colors.green.shade600,
                      ),
                    ),
                  ],
                ),
              );
            }),
          ],
        ),
      ),
    );
  }
}
