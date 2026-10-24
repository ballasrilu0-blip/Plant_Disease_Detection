import 'package:flutter_test/flutter_test.dart';
import 'package:plant_disease_app/main.dart';

void main() {
  testWidgets('PlantDiseaseApp loads home screen', (WidgetTester tester) async {
    await tester.pumpWidget(const PlantDiseaseApp());
    expect(find.text('Plant Disease AI'), findsOneWidget);
    expect(find.text('Take Photo'), findsOneWidget);
    expect(find.text('Gallery'), findsOneWidget);
  });
}
