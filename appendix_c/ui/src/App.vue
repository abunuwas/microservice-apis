<template>
  <div id="nav" style="padding-left: 5px; margin-top: -10px; height: 150px;">
    <nav class="navbar navbar-expand-lg navbar-light">
      <div class="navbar-brand"><h4>CoffeeMesh</h4></div>
      <div class="collapse navbar-collapse" id="navbarSupportedContent">
        <a class="navbar-brand menu" v-if="!$auth.isAuthenticated.value" @click="login">Register</a>
        <a class="navbar-brand menu" v-if="!$auth.isAuthenticated.value" @click="login">Login</a>
        <a class="navbar-brand menu" @click="logout" v-if="$auth.isAuthenticated.value">Logout</a>
      </div>
    </nav>
  </div>

  <div class="container-fluid" style="margin: 5px;">

    <button class="btn btn-primary" @click="showOrders = !showOrders">Show my orders</button>
    <div class="row row-cols-1 row-cols-md-3 g-4" v-if="showOrders" style="margin-top: 10px;">
      <div class="col" v-for="order in orders" :key="order.id">
        <div class="card">
          <div class="card-body">
            <card class="text">
              <div class="row">
                <div class="col col-8">
                  <div v-for="item in order.order" :key="`${order.id}-${item.product}-${item.size}-${item.quantity}`">
                    {{ item.size }} {{ item.product }} x {{ item.quantity }}
                  </div>
                </div>
                <div class="col col-4">
                  <div style="background-color: aqua; padding: 5px; text-align: center; border-radius: 20px;">{{ order.status }}</div>
                </div>
              </div>
            </card>
          </div>
          <div class="card-footer">
            <small class="text-muted">{{ order.created.toLocaleString() }}</small>
          </div>
        </div>
      </div>

    </div>


    <div>Authentication details</div>
    <div>Your token <span><img :src="copyIcon" alt="copy-auth-token" style="width: 1%; min-width: 15px;" class="copy-icon" @click="copyToken"></span></div>
    <div class="token-area" @click="copyToken">{{ this.authToken }}</div>

    <div style="min-height: 50vh">
      <div class="card-group">
        <div class="card" v-for="product in products" :key="product.id" style="margin: 15px; border: 1px solid black;">
          <div class="card-body">
            <div class="card-title">{{ product.name }}</div>
            <div class="row">
              <div class="col-7">
                <select class="form-select" style="min-height: 40px;" v-model="product.selectedSize">
                  <option v-for="size in product.sizes" :value="size" :key="`${product.id}-${size.size}`">
                    {{ size.size }} - ${{ size.price }}
                  </option>
                </select>
              </div>
              <div class="col-5">
                <button class="btn btn-success" style="width: 100%" @click="addItemToBasket(product)">Add</button>
              </div>
            </div>
          </div>
        </div>
      </div>

      <div style="text-align: center; margin-top: 2%" class="container-fluid" v-if="basket.length > 0">
        <div class="row">
          <div class="col-4"></div>
          <div class="col-4" style="border: 1px solid black">
            <div><img :src="shoppingCartIcon" alt="shopping cart" style="width: 5%; margin: 20px"></div>
            <!--          <small>Icons made by <a href="https://www.flaticon.com/authors/azmianshori" title="azmianshori">azmianshori</a> from <a href="https://www.flaticon.com/" title="Flaticon">www.flaticon.com</a></small>-->
            <div class="card" v-for="item in basket" :key="item.id">
              <div class="card-body">
                <div class="row">
                  <div class="col-10">
                    <div class="card-title">{{ item.quantity}} x {{ item.product }} - {{ item.size }}</div>
                  </div>
                  <div class="col-2 delete-item-button" @click="deleteItem(item)">x</div>
                </div>
              </div>
            </div>
          </div>
          <div class="col-4"></div>
        </div>

        <div style="text-align: center; margin-top: 2%; margin-bottom: 5%;">
          <button class="btn btn-primary" @click="checkout">Check out</button>
        </div>
      </div>
    </div>
  </div>

  <div id="bottom" class="container-fluid" style="padding-top: 0; min-height: 80px;">
    <div style="padding-top: 10px;">
      <a href="https://microapis.io" target="_blank"><img :src="microapis" style="width: 1.8rem; margin: 10px" alt="microapis.io"></a>
      <a href="https://github.com/abunuwas/microservice-apis" target="_blank"><img :src="github" style="width: 2rem; margin: 10px" alt="github"></a>
      <a href="https://twitter.com/microapis" target="_blank"><img :src="twitter" style="width: 2rem; margin: 10px" alt="twitter"></a>
      <a href="https://www.reddit.com/r/microapis/" target="_blank"><img :src="reddit" style="width: 2rem; margin: 10px" alt="reddit"></a>
      <a href="https://www.youtube.com/channel/UCtrp0AWmJJXb50zb12XxTlQ" target="_blank"><img :src="youtube" style="width: 2.5rem; margin: 10px" alt="reddit"></a>
    </div>
  </div>
</template>

<script lang="ts">
import axios from "axios";
import { defineComponent } from "vue";
import { products } from "./products";

interface appData {
  products: any,
  basket: Array<any>,
  orders: Array<any>,
  showOrders: Boolean,
  selectedSize: any,
  authToken: null | string
}

export default defineComponent({
  data() {
    return {
      products: products,
      basket: [],
      orders: [],
      showOrders: false,
      selectedSize: null,
      microapis: require('../public/microapis.png'),
      github: require('../public/github.png'),
      twitter: require('../public/twitter.png'),
      reddit: require('../public/reddit.png'),
      youtube: require('../public/youtube.png'),
      shoppingCartIcon: require('../public/shopping-cart.png'),
      copyIcon: require('../public/copy.png'),
      authToken: null
    } as appData
  },
  beforeCreate() {
    products.forEach(product => product.selectedSize = product.sizes[0])
    console.log(products)
  },
  async mounted() {
    // @ts-ignore
    console.log(this.$auth.isAuthenticated.value)
    // @ts-ignore
    this.authToken = await this.$auth.getTokenSilently()
    // @ts-ignore
    console.log(await this.$auth.getIdTokenClaims())
    // @ts-ignore
    console.log(this.$auth.user.value)
    // @ts-ignore
    this.orders = await this.getOrders();
  },
  methods: {
    login() {
      // @ts-ignore
      this.$auth.loginWithRedirect();
    },
    logout() {
      // @ts-ignore
      this.$auth.logout({
        returnTo: window.location.origin
      });
    },
    addItemToBasket(itemToAdd: any) {
      // @ts-ignore
      const itemToAddId = `${itemToAdd.id}-${itemToAdd.selectedSize.size}`
      if (!this.basket.map(addedItem => addedItem.id).includes(itemToAddId)) {
        this.basket.push({
          id: itemToAddId,
          product: itemToAdd.name,
          size: itemToAdd.selectedSize.size,
          quantity: 1
        })
      } else {
        const item = this.basket.filter(item => item.id === itemToAddId)[0]
        item.quantity++
      }
    },
    deleteItem(itemToDelete: any) {
      this.basket.splice(this.basket.indexOf(itemToDelete), 1)
    },
    async checkout() {
      const payload = this.basket.map(item => {
        return {
          product: item.product,
          size: item.size,
          quantity: item.quantity
        }
      })
      try {
        const response = await axios.post(
          `${process.env.VUE_APP_BASE_URL}/orders`,
          {order: payload},
          {headers: {Authorization: `Bearer ${this.authToken}`}}
        )
        this.orders.push(response.data)
      } catch (error) {
        console.log(error.response)
      }
    },
    async getOrders() {
      try {
        const response = await axios.get(
          `${process.env.VUE_APP_BASE_URL}/orders`,
          {headers: {Authorization: `Bearer ${this.authToken}`}}
        )
        // @ts-ignore
        return response.data.orders.map(order => {
          return {
            ...order,
            created: new Date(order.created),
          }
        })
      } catch (error) {
        console.log(error.response)
      }
    } ,
    copyToken() {
      // @ts-ignore
      navigator.clipboard.writeText(this.authToken);
    }
  }
})
</script>
<style scoped>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  color: #2c3e50;
}

#nav a {
  font-weight: bold;
  color: #2c3e50;
}

#nav a.router-link-exact-active {
  color: #42b983;
}

#bottom {
  width: 100%;
  background-color: #2c3e50;
  color: azure;
  text-align: center;
  margin-top: 100px;
  bottom: 0;
}

ul {
  list-style-type: none;
  margin: 0;
  padding: 0;
}

#logo,
.menu:hover {
  cursor: pointer
}

.navbar-brand {
  width: 150px;
  height: 100%;
  padding-right: 20px;
}

.navbar-toggler{
  border: 1px solid white !important;
  color: white;
}

.nav-item a:hover {
  background-color: #e8e8e8;
}

.delete-item-button:hover {
  cursor: pointer;
}

.copy-icon:hover {
  cursor: pointer;
}

.token-area {
  max-width: 90%;
  overflow-wrap: break-word;
  padding: 10px;
  background-color: #f2f2f2;
  border-radius: 20px;
  margin-top: 5px;
}

.token-area:hover {
  cursor: pointer;
}
</style>
