class TopPrediction {
  final String modelClass;
  final String disease;
  final String plant;
  final double confidence;

  TopPrediction({
    required this.modelClass,
    required this.disease,
    required this.plant,
    required this.confidence,
  });

  factory TopPrediction.fromJson(Map<String, dynamic> json) {
    return TopPrediction(
      modelClass: json['model_class'] ?? '',
      disease: json['disease'] ?? 'Unknown',
      plant: json['plant'] ?? 'Unknown',
      confidence: (json['confidence'] as num?)?.toDouble() ?? 0.0,
    );
  }
}

class DiseaseResult {
  final String modelClass;
  final String disease;
  final String plant;
  final String affectedPart;
  final String diseaseType;
  final double confidence;
  final bool isHealthy;
  final bool knowledgeAvailable;
  final String cause;
  final String pathogen;
  final List<String> symptoms;
  final List<String> whyItHappens;
  final List<String> favorableConditions;
  final List<String> prevention;
  final List<String> immediateAction;
  final List<String> culturalControl;
  final List<String> biologicalControl;
  final String chemicalControl;
  final String safetyWarning;
  final List<TopPrediction> topPredictions;

  DiseaseResult({
    required this.modelClass,
    required this.disease,
    required this.plant,
    required this.affectedPart,
    required this.diseaseType,
    required this.confidence,
    required this.isHealthy,
    required this.knowledgeAvailable,
    required this.cause,
    required this.pathogen,
    required this.symptoms,
    required this.whyItHappens,
    required this.favorableConditions,
    required this.prevention,
    required this.immediateAction,
    required this.culturalControl,
    required this.biologicalControl,
    required this.chemicalControl,
    required this.safetyWarning,
    required this.topPredictions,
  });

  static List<String> _parseStringList(dynamic value) {
    if (value is List) {
      return value.map((item) => item.toString()).where((s) => s.isNotEmpty).toList();
    }
    if (value is String && value.trim().isNotEmpty) {
      return [value.trim()];
    }
    return [];
  }

  factory DiseaseResult.fromJson(Map<String, dynamic> json) {
    var rawTop = json['top_predictions'] as List<dynamic>? ?? [];
    List<TopPrediction> topList = rawTop
        .map((item) => TopPrediction.fromJson(item as Map<String, dynamic>))
        .toList();

    String chem = '';
    if (json['chemical_control'] is List) {
      chem = (json['chemical_control'] as List).join('\n• ');
      if (chem.isNotEmpty) chem = '• $chem';
    } else if (json['chemical_control'] != null) {
      chem = json['chemical_control'].toString();
    }

    return DiseaseResult(
      modelClass: json['model_class'] ?? '',
      disease: json['disease'] ?? 'Unknown',
      plant: json['plant'] ?? 'Unknown',
      affectedPart: json['affected_part'] ?? 'Unknown',
      diseaseType: json['disease_type'] ?? 'Unknown',
      confidence: (json['confidence'] as num?)?.toDouble() ?? 0.0,
      isHealthy: json['healthy'] == true,
      knowledgeAvailable: json['knowledge_available'] == true,
      cause: json['cause']?.toString() ?? '',
      pathogen: json['pathogen']?.toString() ?? '',
      symptoms: _parseStringList(json['symptoms']),
      whyItHappens: _parseStringList(json['why_it_happens']),
      favorableConditions: _parseStringList(json['favorable_conditions']),
      prevention: _parseStringList(json['prevention']),
      immediateAction: _parseStringList(json['immediate_action']),
      culturalControl: _parseStringList(json['cultural_control']),
      biologicalControl: _parseStringList(json['biological_control']),
      chemicalControl: chem,
      safetyWarning: json['safety_warning']?.toString() ?? '',
      topPredictions: topList,
    );
  }
}
