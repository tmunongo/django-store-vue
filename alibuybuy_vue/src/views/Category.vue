<template lang="">
  <div className="flex flex-col justify-center">
    <div className="flex items-start justify-center">
      <div v-for="products in category.products" v-bind:key="products.id">
        <div>
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
  name: "Category",
  data() {
    return {
      category: {
        products: [],
      },
    };
  },
  mounted() {
    this.getCategory();
  },
  watch: {
    $route(to, from) {
      if (to.name === "Category") {
        this.getCategory();
      }
    },
  },
  methods: {
    async getCategory() {
      const categorySlug = this.$route.params.category_slug;
      this.$store.commit("setIsLoading", true);
      axios
        .get(`/api/v1/products/${categorySlug}/`)
        .then((response) => {
          console.log(response.data);
          this.category = response.data;
          document.title = this.category.name + " | AliBuyBuy";
        })
        .catch((err) => {
          console.log(err);
        });

      this.$store.commit("setIsLoading, false");
    },
  },
};
</script>
<style lang=""></style>
