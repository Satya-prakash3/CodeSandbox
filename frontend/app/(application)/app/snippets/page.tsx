export default function SnippetsPage() {
  return (
    <section className="p-6">
      <h2 className="text-2xl font-bold text-gray-900 mb-6">Snippets</h2>
      <p className="text-gray-600">
        Manage your code snippets here. Create, share, and analyze snippets securely.
      </p>
      <div className="mt-6 bg-white p-4 rounded-lg shadow">
        <h3 className="font-medium text-gray-800 mb-2">Your Snippets</h3>
        <p className="text-gray-500">No snippets found.</p>
      </div>
    </section>
  );
}