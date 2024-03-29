import { initMercadoPago, CardPayment } from "@mercadopago/sdk-react"
import { storePayment } from "./services"

initMercadoPago(import.meta.env.VITE_MERCADOPAGO_PUBLIC_KEY)

export default function App() {
  const initialization = {
    amount: 500,
  }

  const handleOnSubmit = async (formData) => {
    await storePayment(formData)
  }

  return (
    <>
      <h1>Pagando con mercado pago</h1>
      <CardPayment 
      initialization={initialization}
      onSubmit={handleOnSubmit}
      customization={{
        paymentMethods: {
          maxInstallments: 1,
        },
        visual: {
          style: {
            theme: "dark",
          }
        }
      }}
      />
    </>
  )
}