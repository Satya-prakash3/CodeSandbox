export default function VerifyEmailPage() {
  return (
    <div className="bg-white p-8 rounded-lg shadow-md">
      <h2 className="text-2xl font-bold text-gray-900 mb-6">Verify Email</h2>
      <p className="text-gray-700">
        A verification email has been sent to your address. Please check your inbox and click the link to verify your email address.
      </p>
      <div className="mt-8">
        <p className="text-gray-600 text-sm">If you didn&apos;t receive the email, please <a href="#" className="text-emerald-600 hover:text-emerald-700">request another</a>.</p>
      </div>
    </div>
  );
};