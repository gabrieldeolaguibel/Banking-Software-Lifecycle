<template>
  <div id="app">
    <nav>
      <router-link to="/">Home</router-link> |
      <router-link to="/skull">Skull</router-link> |
      <router-link to="/accounts">Accounts</router-link>
    </nav>
    <router-view/>
  </div>
</template>

<style>
#app {
  margin-top: 60px;
}
</style>
