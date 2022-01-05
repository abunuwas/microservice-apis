enum size {
  Small = 'small',
  Medium = 'medium',
  Big = 'big'
}

interface product {
  id: string,
  name: string,
  sizes: any,
  selectedSize?: string
}

export const products = [
  {
    id: 'fa52dd1d-7d19-4342-92f7-0801b568760f',
    name: 'Cappuccino',
    sizes: [
      {
        size: size.Small,
        price: 10
      },
      {
        size: size.Medium,
        price: 12
      },
      {
        size: size.Big,
        price: 14
      },
    ]
  },
  {
    id: 'f14c1a98-6c55-4866-a36b-0fdab61bfcb4',
    name: 'Mocha',
    sizes: [
      {
        size: size.Small,
        price: 12
      },
      {
        size: size.Medium,
        price: 16
      },
      {
        size: size.Big,
        price: 20
      },
    ]
  },
  {
    id: '7dafe3c2-0991-42a6-b1bf-789ace4b1fe0',
    name: 'Espresso',
    sizes: [
      {
        size: size.Small,
        price: 8
      },
      {
        size: size.Medium,
        price: 24
      },
      {
        size: size.Big,
        price: 30
      },
    ]
  },
  {
    id: 'd64efb9b-a731-401e-a52a-49a4f5754dfc',
    name: 'Taro Bubble Tea',
    sizes: [
      {
        size: size.Small,
        price: 18
      },
      {
        size: size.Medium,
        price: 29
      },
      {
        size: size.Big,
        price: 35
      },
    ]
  }
] as Array<product>
