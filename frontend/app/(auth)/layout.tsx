export default function AuthLayout({
  children,
}: {
  children: React.ReactNode;
}) {
  return (
    <div className="min-h-screen flex flex-col">
      <header className="bg-white shadow">
        <div className="max-w-7xl mx-auto px-4 py-6 sm:px-6 lg:px-8">
          <div className="flex justify-between items-center">
            <h1 className="text-2xl font-bold text-gray-900">
              Account
            </h1>
          </div>
        </div>
      </header>

      <main className="flex-1 max-w-md mx-auto px-4 py-6 sm:px-6 lg:px-8">
        {children}
      </main>

      <footer className="bg-white shadow mt-auto">
        <div className="max-w-7xl mx-auto px-4 py-6 sm:px-6 lg:px-8 text-center text-gray-600 text-sm">
          © 2026 CodeSandbox. All rights reserved.
        </div>
      </footer>
    </div>
  );
}