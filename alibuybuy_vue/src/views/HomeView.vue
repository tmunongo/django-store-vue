<template>
  <div class="home w-screen">
    <div
      class="mb-6 bg-gray-600 text-white h-[60vh] w-full flex flex-col items-center justify-center"
    >
      <h2 class="mb-6 font-bold text-3xl">Welcome to AliBuyBuy</h2>
      <p class="mb-6 text-lg">Where prices respect your budget</p>
    </div>
    <div class="flex flex-col justify-start items-center">
      <div>
        <h2 class="mb-6 font-bold text-2xl">Latest Products</h2>
      </div>
      <div
        class="flex md:flex-row flex-col justify-center items-center w-[100%] p-4"
      >
        <div v-for="products in latestProducts" v-bind:key="products.id">
          <div
            class="border flex items-center justify-around flex-col rounded-md shadow-md h-80 w-80 m-2"
          >
            <div class="overflow-hidden">
              <img v-bind:src="products.get_thumbnail" class="m-[-1.25rem]" />
            </div>
            <h3 class="text-lg">{{ products.name }}</h3>
            <p class="text-base text-gray-700">${{ products.price }}</p>

            <router-link
              v-bind:to="products.get_absolute_url"
              class="shadow-md bg-[#ff7f50] p-2 rounded-2xl"
            >
              View Details
            </router-link>
          </div>
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
