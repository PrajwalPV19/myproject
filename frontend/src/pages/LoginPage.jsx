export default function LoginPage() {
  return (
    <div className="min-h-screen grid place-items-center">
      <form className="bg-white shadow rounded-xl p-8 w-full max-w-md space-y-4">
        <h2 className="text-2xl font-bold">Login</h2>
        <input className="w-full border rounded p-2" placeholder="Email" />
        <input className="w-full border rounded p-2" placeholder="Password" type="password" />
        <button className="w-full bg-slate-900 text-white p-2 rounded">Sign In</button>
      </form>
    </div>
  )
}
