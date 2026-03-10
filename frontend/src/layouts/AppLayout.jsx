import { Link, Outlet } from 'react-router-dom'

const nav = [
  ['Dashboard', '/'],
  ['Clients', '/clients'],
  ['Invoices', '/invoices'],
  ['Create Invoice', '/invoices/new'],
  ['Reports', '/reports'],
  ['Settings', '/settings']
]

export default function AppLayout() {
  return (
    <div className="min-h-screen flex">
      <aside className="w-64 bg-slate-900 text-white p-4 space-y-2">
        <h1 className="text-xl font-bold">SmartInvoice</h1>
        {nav.map(([label, path]) => (
          <Link className="block py-2 hover:text-cyan-300" key={path} to={path}>{label}</Link>
        ))}
      </aside>
      <main className="flex-1 p-8"><Outlet /></main>
    </div>
  )
}
