<template>
  <div class="home">
    <div
      class="mb-6 bg-gray-600 text-white h-[60vh] w-screen flex flex-col items-center justify-center"
    >
      <h2 class="mb-6 font-bold text-3xl">Welcome to AliBuyBuy</h2>
      <p class="mb-6 text-lg">Where prices respect your budget</p>
    </div>
    <div class="flex flex-col justify-start items-center">
      <div>
        <h2 class="mb-6 font-bold text-2xl">Latest Products</h2>
      </div>
      <div v-for="products in latestProducts" v-bind:key="products.id">
        <div class="">
          <div>
            <img v-bind:src="products.get_thumbnail" class="m-[-1.25rem]" />
          </div>
          <h3 class="text-lg">{{ products.name }}</h3>
          <p class="text-base text-gray-700">${{ products.price }}</p>

          <button>View Details</button>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import axios from "axios";

export default {
  name: "HomeView",
  data() {
    return {
      latestProducts: [],
    };
  },
  components: {},
  mounted() {
    this.getLatestProducts();
  },
  methods: {
    getLatestProducts() {
      axios
        .get("/api/v1/latest-products")
        .then((response) => {
          this.latestProducts = response.data;
        })
        .catch((error) => {
          console.log(error);
        });
    },
  },
};
</script>
