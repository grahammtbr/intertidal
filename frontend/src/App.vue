<script setup>
// import { RouterLink, RouterView } from 'vue-router'
import SiteHeader from './components/SiteHeader.vue'
import MapView from './views/MapView.vue'
</script>

<template>
    <!-- <header>
    <img alt="Vue logo" class="logo" src="@/assets/logo.svg" width="125" height="125" />

    <div class="wrapper">
      <HelloWorld msg="You did it!" />

      <nav>
        <RouterLink to="/">Home</RouterLink>
        <RouterLink to="/intertidal">Intertidal</RouterLink>
      </nav>
    </div>
  </header> -->

    <!-- <RouterView /> -->
    <SiteHeader />
    <MapView />
</template>
