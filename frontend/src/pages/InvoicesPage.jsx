import { Link } from 'react-router-dom'

export default function InvoicesPage() {
  return (
    <div>
      <div className="flex justify-between items-center mb-4">
        <h2 className="text-3xl font-bold">Invoices</h2>
        <Link to="/invoices/new" className="bg-cyan-600 text-white px-4 py-2 rounded">New Invoice</Link>
      </div>
      <div className="bg-white rounded-xl shadow p-4">INV-2026-001 • Sent • ₹24,900</div>
    </div>
  )
}
