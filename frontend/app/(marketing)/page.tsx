export default function MarketingPage() {
  return (
    <div className="min-h-screen bg-background text-foreground">
      <div className="max-w-7xl mx-auto px-4 py-6 sm:px-6 lg:px-8">
        <h1 className="text-4xl font-bold text-gray-900 sm:text-5xl mb-6">
          Secure Code Analysis
        </h1>
        <p className="text-lg text-gray-700 mb-8">
          Execute code in isolated environments. Share results securely.
        </p>
        <div className="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-3 gap-8">
          <div className="bg-white p-6 rounded-lg shadow">
            <h2 className="text-xl font-semibold text-gray-800 mb-4">Features</h2>
            <ul className="list-disc list-inside space-y-2 text-gray-700">
              <li>Code execution in isolated environments</li>
              <li>Secure sharing and collaboration</li>
              <li>Multi-language support</li>
              <li>Real-time feedback</li>
            </ul>
          </div>
          <div className="bg-white p-6 rounded-lg shadow">
            <h2 className="text-xl font-semibold text-gray-800 mb-4">How It Works</h2>
            <ol className="list-decimal list-inside space-y-2 text-gray-700">
              <li>Write or paste your code</li>
              <li>Select execution options</li>
              <li>Run with one click</li>
              <li>View analysis results</li>
            </ol>
          </div>
          <div className="bg-white p-6 rounded-lg shadow">
            <h2 className="text-xl font-semibold text-gray-800 mb-4">Security</h2>
            <p className="text-gray-700">
              Code runs in isolated environments with appropriate safeguards.
            </p>
          </div>
        </div>
        <div className="mt-12 text-center">
          <a
            href="/login"
            className="inline-block bg-emerald-600 text-white px-6 py-3 rounded-md hover:bg-emerald-700 transition"
          >
            Get Started
          </a>
        </div>
      </div>
    </div>
  );
}