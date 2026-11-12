import Link from 'next/link';

export default function MarketingLayout({
  children,
}: {
  children: React.ReactNode;
}) {
  return (
    <div className="min-h-screen flex flex-col">
      <header className="bg-white shadow">
        <nav className="max-w-7xl mx-auto px-4 py-6 sm:px-6 lg:px-8">
          <div className="flex justify-between h-16">
            <div className="flex">
              <Link href="/" className="text-xl font-bold text-gray-900">
                CodeSandbox
              </Link>
            </div>
            <div className="hidden sm:ml-6 sm:flex sm:items-center">
              <Link href="/login" className="text-gray-600 hover:text-gray-900">
                Sign In
              </Link>
              <Link href="/register" className="ml-4 text-gray-600 hover:text-gray-900">
                Register
              </Link>
            </div>
          </div>
        </nav>
      </header>

      <main className="flex-1 max-w-7xl mx-auto px-4 py-6 sm:px-6 lg:px-8">
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