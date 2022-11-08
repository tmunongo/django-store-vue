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
        <ProductBox
          v-for="products in latestProducts"
          v-bind:key="products.id"
          v-bind:products="products"
        />
      </div>
    </div>
  </div>
</template>

<script>
import axios from "axios";

import ProductBox from "@/components/ProductBox";

export default {
  name: "HomeView",
  data() {
    return {
      latestProducts: [],
    };
  },
  components: {
    ProductBox,
  },
  mounted() {
    this.getLatestProducts();
    document.title = "Home | AliBuyBuy";
  },
  methods: {
    async getLatestProducts() {
      this.$store.commit("setIsLoading", true);
      await axios
        .get("/api/v1/latest-products")
        .then((response) => {
          this.latestProducts = response.data;
        })
        .catch((error) => {
          console.log(error);
        });
      this.$store.commit("setIsLoading", false);
    },
  },
};
</script>
