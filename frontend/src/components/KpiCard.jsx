export default function KpiCard({ title, value }) {
  return (
    <div className="bg-white rounded-xl p-4 shadow">
      <p className="text-sm text-slate-500">{title}</p>
      <h3 className="text-2xl font-semibold">{value}</h3>
    </div>
  )
}
