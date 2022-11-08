<template>
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
</template>

<script>
export default {
  name: "ProductBox",
  props: {
    products: Object,
  },
};
</script>
