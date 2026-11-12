export default function AnalysisPage() {
  return (
    <section className="p-6">
      <h2 className="text-2xl font-bold text-gray-900 mb-6">Analysis</h2>
      <p className="text-gray-600">
        View code analysis results and security assessments here.
      </p>
      <div className="mt-6 bg-white p-4 rounded-lg shadow">
        <h3 className="font-medium text-gray-800 mb-2">Analysis History</h3>
        <p className="text-gray-500">No analysis found.</p>
      </div>
    </section>
  );
};