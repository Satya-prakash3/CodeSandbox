import Link from 'next/link';

export default function ApplicationLayout({
  children,
}: {
  children: React.ReactNode;
}) {
  return (
    <div className="flex min-h-screen flex-col overflow-hidden">
      <aside
        className="bg-gray-900 w-64 h-full text-white flex flex-col border-r border-gray-700 shadow-lg"
        aria-label="Main navigation sidebar"
      >
        <div className="flex h-16 items-center justify-between px-6 border-b border-gray-700">
          <span className="text-xl font-bold">CodeSandbox</span>
          <button
            aria-label="Open menu"
            className="p-2 hover:text-emerald-400"
          >
            ☰
          </button>
        </div>

        <nav className="flex-1 flex flex-col p-4 space-y-2">
          <Link
            href="/app/dashboard"
            className="group flex items-center px-3 py-2 rounded-md text-sm text-gray-300 hover:text-white hover:bg-gray-800 transition-colors"
            aria-label="Dashboard"
          >
            <span className="shrink me-2">📊</span>
            Dashboard
          </Link>

          <Link
            href="/app/snippets"
            className="group flex items-center px-3 py-2 rounded-md text-sm text-gray-300 hover:text-white hover:bg-gray-800 transition-colors"
            aria-label="Snippets"
          >
            <span className="shrink me-2">📁</span>
            Snippets
          </Link>

          <Link
            href="/app/analysis"
            className="group flex items-center px-3 py-2 rounded-md text-sm text-gray-300 hover:text-white hover:bg-gray-800 transition-colors"
            aria-label="Analysis"
          >
            <span className="shrink me-2">🔍</span>
            Analysis
          </Link>

          <Link
            href="/app/settings"
            className="group flex items-center px-3 py-2 rounded-md text-sm text-gray-300 hover:text-white hover:bg-gray-800 transition-colors"
            aria-label="Settings"
          >
            <span className="shrink me-2">⚙️</span>
            Settings
          </Link>
        </nav>
      </aside>

      <div className="flex-1 flex flex-col overflow-hidden">
        <header
          className="bg-gray-900 text-white h-16 flex items-center justify-between px-6 border-b border-gray-700"
        >
          <div className="flex items-center gap-6">
            <span className="text-xl font-bold">CodeSandbox</span>
            <div className="flex items-center gap-4 text-sm text-gray-400">
              <span>Satyaprakash Sethy</span>
            </div>
          </div>
        </header>

        <main
          className="flex-1 overflow-auto p-6 sm:p-8 lg:p-8"
          aria-label="Main content area"
        >
          {children}
        </main>

        <footer
          className="bg-gray-900 text-white text-sm py-4 border-t border-gray-700"
        >
          <div className="max-w-7xl mx-auto px-6 text-center">
            © 2026 CodeSandbox. All rights reserved.
          </div>
        </footer>
      </div>
    </div>
  );
}