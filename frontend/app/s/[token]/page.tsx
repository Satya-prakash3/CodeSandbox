
type PublicSharingPageProps = {
  params: Promise<{
    token: string;
  }>;
};

export default async function PublicSharingPage({
  params,
}: PublicSharingPageProps) {
  // Resolve the dynamic route parameters.
  // The token will be used for backend permission verification later.
  await params;

  return (
    <main className="p-6">
      <h1 className="mb-6 text-2xl font-bold text-gray-900">
        Code Snippet
      </h1>

      <p className="text-gray-600">
        Public snippet access requires permission verification.
      </p>

      <div className="mt-6 rounded-lg bg-white p-4 shadow">
        <p className="text-gray-500">
          Snippet content will be displayed after backend
          authorization.
        </p>
      </div>
    </main>
  );
}
