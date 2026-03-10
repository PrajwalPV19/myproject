export default function ClientsPage() {
  return (
    <div>
      <h2 className="text-3xl font-bold mb-4">Clients</h2>
      <div className="bg-white rounded-xl shadow overflow-hidden">
        <table className="w-full text-left">
          <thead className="bg-slate-100"><tr><th className="p-3">Name</th><th>Email</th><th>Status</th></tr></thead>
          <tbody><tr><td className="p-3">Acme Ltd</td><td>finance@acme.com</td><td>Active</td></tr></tbody>
        </table>
      </div>
    </div>
  )
}
