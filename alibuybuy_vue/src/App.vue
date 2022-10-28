<template>
  <div
    id="wrapper"
    class="flex flex-col justify-start items-center min-h-screen w-screen"
  >
    <div
      class="flex justify-around items-center h-20 p-1 bg-[#E1E2EF] w-screen"
    >
      <div class="max-w-max">
        <router-link to="/" class="">
          <strong> AliBuyBuy </strong>
        </router-link>
        <a aria-label="menu" aria-expanded="false" data-target="navbar-menu">
          <span aria-hidden="true"></span>
          <span aria-hidden="true"></span>
          <span aria-hidden="true"></span>
        </a>
      </div>
      <div class="">
        <div class="flex items-center justify-around">
          <div class="hidden md:block">
            <Menu>
              <MenuButton>Categories</MenuButton>
              <MenuItems>
                <MenuItem>
                  <router-link to="/used" class="mx-1">Used</router-link>
                </MenuItem>
                <MenuItem>
                  <router-link
                    to="/new"
                    class="mx-1 hover:bg-opacity-50 hover:transition-all"
                    >New</router-link
                  >
                </MenuItem>
              </MenuItems>
            </Menu>
          </div>

          <div class="">
            <div class="flex items-center justify-center">
              <router-link
                to="/login"
                class="h-10 p-1 bg-[#E2C044] rounded-md m-2 hover:scale-110 transition-all duration-500 w-20 text-center"
                >Log In</router-link
              >
              <router-link
                to="/cart"
                class="h-10 p-1 bg-[#D81E5B] w-[90px] rounded-md m-2 hover:scale-110 transition-all duration-500"
              >
                <span class="flex justify-around items-center">
                  <img
                    src="https://icongr.am/fontawesome/shopping-cart.svg?size=16&color=currentColor"
                    alt="cart"
                  />
                  <span>Cart ({{ cartTotalLength }})</span>
                </span>
              </router-link>
            </div>
          </div>
          <div class="md:hidden cursor-grab">
            <img
              src="https://icongr.am/fontawesome/align-justify.svg?size=32&color=currentColor"
              alt="menu"
              @click="showMobileMenu = !showMobileMenu"
            />
          </div>
          <!-- <div
            class="flex items-center justify-center"
            v-bind:class="{ 'is-active': showMobileMenu }"
          >
            <ul>
              <li>
                <router-link
                  to="/new"
                  class="mx-1 hover:bg-opacity-50 hover:transition-all"
                  >New</router-link
                >
              </li>
              <li>
                <router-link to="/used" class="mx-1">Used</router-link>
              </li>
            </ul>
          </div> -->
        </div>
      </div>
    </div>
    <div
      class="text-center"
      v-bind:class="{ 'is-loading': $store.state.isLoading }"
    >
      <div class="lds-ripple"></div>
    </div>
    <section class="flex min-h-[60vh] w-[100%]">
      <router-view />
    </section>
    <footer
      class="flex items-center justify-center bg-[#E1E2EF] h-[30vh] w-screen"
    >
      <p class="">
        <a href="www.tawandamunongo.tech"> Explore My Other Work</a>
      </p>
    </footer>
  </div>
</template>

<script setup>
import { Menu, MenuButton, MenuItem, MenuItems } from "@headlessui/vue";
</script>

<script>
export default {
  data() {
    return {
      showMobileMenu: false,
      cart: {
        items: [],
      },
    };
  },
  beforeCreate() {
    this.$store.commit("initializeStore");
  },
  mounted() {
    this.cart = this.$store.state.cart;
  },
  computed: {
    cartTotalLength() {
      let totalLength = 0;

      for (let index = 0; index < this.cart.items.length; index++) {
        totalLength += this.cart.items[index].quantity;
      }

      return totalLength;
    },
  },
};
</script>

<style>
@import "./app.css";
.lds-ripple {
  display: inline-block;
  position: relative;
  width: 80px;
  height: 80px;
}
.lds-ripple div {
  position: absolute;
  border: 4px solid #fff;
  opacity: 1;
  border-radius: 50%;
  animation: lds-ripple 1s cubic-bezier(0, 0.2, 0.8, 1) infinite;
}
.lds-ripple div:nth-child(2) {
  animation-delay: -0.5s;
}
@keyframes lds-ripple {
  0% {
    top: 36px;
    left: 36px;
    width: 0;
    height: 0;
    opacity: 0;
  }
  4.9% {
    top: 36px;
    left: 36px;
    width: 0;
    height: 0;
    opacity: 0;
  }
  5% {
    top: 36px;
    left: 36px;
    width: 0;
    height: 0;
    opacity: 1;
  }
  100% {
    top: 0px;
    left: 0px;
    width: 72px;
    height: 72px;
    opacity: 0;
  }
}
</style>
