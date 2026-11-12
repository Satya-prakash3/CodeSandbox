'use client';


export default function Error({
  reset,
}: {
  error: Error;
  reset: () => void;
}) {
  return (
    <div className="min-h-screen bg-white p-8 flex flex-col items-center justify-center">
      <h2 className="text-2xl font-bold text-gray-900 mb-4">Something went wrong</h2>
      <p className="text-gray-600 mb-8 max-w-2xl text-center">
        An unexpected error occurred. Please try again.
      </p>
      <button
        onClick={reset}
        className="inline-block bg-emerald-600 text-white px-6 py-3 rounded-md hover:bg-emerald-700 transition"
      >
        Reset
      </button>
    </div>
  );
}