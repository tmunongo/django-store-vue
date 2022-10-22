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
                class="h-8 p-1 bg-[#E2C044] rounded-md m-2 hover:scale-110 transition-all duration-500"
                >Log In</router-link
              >
              <router-link
                to="/cart"
                class="h-8 p-1 bg-[#D81E5B] w-16 rounded-md m-2 hover:scale-110 transition-all duration-500"
              >
                <span class="flex justify-around items-center">
                  <img
                    src="https://icongr.am/fontawesome/shopping-cart.svg?size=16&color=currentColor"
                    alt="cart"
                  />
                  <span>Cart</span>
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
    <section class="flex min-h-[60vh]">
      <router-view />
    </section>
    <footer
      class="flex items-center justify-center bg-[#E1E2EF] h-[30vh] w-screen"
    >
      <p class="">
        <a href="www.tawandamunongo.tech"> Built By </a>
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
    };
  },
};
</script>

<style lang="scss">
@import "./app.css";
</style>
