export default function DashboardPage() {
  return (
    <section className="p-6">
      <h2 className="text-2xl font-bold text-gray-900 mb-6">Dashboard</h2>
      <p className="text-gray-600">
        Welcome to your CodeSandbox dashboard. Here you can manage your code snippets and view analysis results.
      </p>
      <div className="mt-6 grid grid-cols-1 sm:grid-cols-2 gap-4">
        <div className="bg-white p-4 rounded-lg shadow">
          <h3 className="font-medium text-gray-800 mb-2">Recent Snippets</h3>
          <p className="text-gray-500">No snippets yet.</p>
        </div>
        <div className="bg-white p-4 rounded-lg shadow">
          <h3 className="font-medium text-gray-800 mb-2">Recent Analysis</h3>
          <p className="text-gray-500">No analysis yet.</p>
        </div>
      </div>
    </section>
  );
}