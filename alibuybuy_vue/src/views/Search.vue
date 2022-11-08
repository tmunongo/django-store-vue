<template>
  <div class="flex flex-col justify-start items-center w-full">
    <div class="">
      <h1 class="text-2xl m-2 text-center">Search</h1>
      <h2 class="text-lg m-2">Search term: "{{ query }}"</h2>
    </div>
    <div>
      <ProductBox
        v-for="products in products"
        v-bind:key="products.id"
        v-bind:products="products"
      />
    </div>
  </div>
</template>
<script>
import ProductBox from "@/components/ProductBox";

import axios from "axios";

export default {
  name: "Search",
  components: {
    ProductBox,
  },
  data() {
    return {
      products: [],
      query: "",
    };
  },
  mounted() {
    document.title = "Search | AliBuyBuy";

    let uri = window.location.search.substring(1);
    let params = new URLSearchParams(uri);

    if (params.get("query")) {
      this.query = params.get("query");

      this.performSearch();
    }
  },
  methods: {
    async performSearch() {
      this.$store.commit("setIsLoading", true);

      await axios
        .post("/api/v1/products/search/", { query: this.query })
        .then((response) => {
          this.products = response.data;
        })
        .catch((error) => {
          console.log(error);
        });

      this.$store.commit("setIsLoading", false);
    },
  },
};
</script>
<style lang=""></style>
