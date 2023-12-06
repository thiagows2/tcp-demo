import express from 'express'
import { Router, Request, Response } from 'express'

const app = express()
const route = Router()

app.use(express.json())

route.post('/fibonacci', async (req: Request, res: Response) => {
  const { number } = req.body

  try {
    const response = await fetch(`http://127.0.0.1:5000/recursive?n=${number}`, {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json'
      },
    })
    const result = await response.json()

    res.json(result)
  } catch (error) {
    res.json(error)
  }
})

app.use(route)

app.listen(3000, () => 'server running on port 3000')
