<template>
  <div id="product-page" class="flex items-start justify-center w-full">
    <div class="flex flex-col items-center justify-center w-[70%]">
      <figure>
        <img v-bind:src="products.get_image" />
      </figure>

      <h1 class="text-2xl">{{ products.name }}</h1>
      <p>{{ products.description }}</p>
    </div>
    <div class="h-1/2 w-[30%] flex flex-col justify-around items-start">
      <h2 class="text-lg">Information</h2>
      <p><strong>Price: </strong>{{ products.price }}</p>
      <div>
        <div>
          <input
            type="number"
            class="border-2 rounded-md p-2"
            min="1"
            v-model="quantity"
          />
        </div>
        <div class="mt-4">
          <a class="p-2 rounded-md bg-[#ff7f50] cursor-grab" @click="addToCart"
            >Add to cart</a
          >
        </div>
      </div>
    </div>
  </div>
</template>
<script>
import axios from "axios";
export default {
  name: "Products",
  data() {
    return {
      products: {},
      quantity: 1,
    };
  },
  mounted() {
    this.getProducts();
  },
  methods: {
    async getProducts() {
      this.$store.commit("setIsLoading", true);

      const category_slug = this.$route.params.category_slug;
      const product_slug = this.$route.params.product_slug;

      await axios
        .get(`/api/v1/products/${category_slug}/${product_slug}`)
        .then((response) => {
          this.products = response.data;
          document.title = this.products.name + " | AliBuyBuy";
        })
        .catch((error) => {
          console.log(error);
        });
      this.$store.commit("setIsLoading", false);
    },
    addToCart() {
      if (isNaN(this.quantity) || this.quantity < 1) {
        this.quantity = 1;
      }

      const item = {
        products: this.products,
        quantity: this.quantity,
      };
      this.$store.commit("addToCart", item);
    },
  },
};
</script>
<style></style>
