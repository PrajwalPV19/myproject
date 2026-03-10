export default function CreateInvoicePage() {
  return (
    <div className="space-y-4">
      <h2 className="text-3xl font-bold">Create Invoice</h2>
      <div className="bg-white rounded-xl shadow p-6 grid md:grid-cols-2 gap-4">
        <input className="border rounded p-2" placeholder="Client" />
        <input className="border rounded p-2" placeholder="Invoice Number" />
        <input className="border rounded p-2" placeholder="Due Date" type="date" />
        <input className="border rounded p-2" placeholder="GST Rate" type="number" />
      </div>
    </div>
  )
}
