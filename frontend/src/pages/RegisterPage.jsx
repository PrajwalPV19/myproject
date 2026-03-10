export default function RegisterPage() {
  return (
    <div className="min-h-screen grid place-items-center">
      <form className="bg-white shadow rounded-xl p-8 w-full max-w-md space-y-4">
        <h2 className="text-2xl font-bold">Register</h2>
        <input className="w-full border rounded p-2" placeholder="Full Name" />
        <input className="w-full border rounded p-2" placeholder="Email" />
        <input className="w-full border rounded p-2" placeholder="Password" type="password" />
        <button className="w-full bg-cyan-600 text-white p-2 rounded">Create Account</button>
      </form>
    </div>
  )
}
