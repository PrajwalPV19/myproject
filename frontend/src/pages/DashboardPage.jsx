import { Bar } from 'react-chartjs-2'
import { Chart as ChartJS, CategoryScale, LinearScale, BarElement } from 'chart.js'
import KpiCard from '../components/KpiCard'

ChartJS.register(CategoryScale, LinearScale, BarElement)

export default function DashboardPage() {
  const data = { labels: ['Jan', 'Feb', 'Mar'], datasets: [{ label: 'Revenue', data: [12000, 18000, 22000] }] }
  return (
    <div className="space-y-6">
      <h2 className="text-3xl font-bold">Dashboard</h2>
      <div className="grid md:grid-cols-4 gap-4">
        <KpiCard title="Total Revenue" value="₹5,42,000" />
        <KpiCard title="Outstanding" value="₹78,000" />
        <KpiCard title="Paid Invoices" value="184" />
        <KpiCard title="Overdue" value="13" />
      </div>
      <div className="bg-white rounded-xl p-4 shadow"><Bar data={data} /></div>
    </div>
  )
}
