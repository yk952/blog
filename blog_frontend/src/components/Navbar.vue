<template>
  <nav class="navbar">
    <div class="navbar-container">
      <router-link to="/" class="logo">文章平台</router-link>
      <div class="nav-links">
        <router-link to="/" class="nav-link">首页</router-link>
        <router-link to="/post" class="nav-link">发布</router-link>
        <router-link to="/login" class="nav-link login-btn">登录</router-link>
      </div>
    </div>
  </nav>
</template>

<style scoped>
.navbar {
  background-color: var(--yk-card-bg);
  color: var(--yk-fontcolor);
  padding: 1rem 0;
  box-shadow: var(--yk-shadow-nav);
  position: fixed; 
  top: 0; 
  left: 0; 
  right: 0;
  z-index: 999; 
}

.navbar-container {
  max-width: 1200px;
  margin: 0 auto;
  padding: 0 2rem;
  display: flex;
  justify-content: space-between;
  align-items: center;
}

.logo {
  color: var(--yk-fontcolor);
  text-decoration: none;
  font-size: 1.5rem;
  font-weight: bold;
  transition: color 0.3s;
}
.logo:hover {
  color: var(--yk-hovertext);
}

.nav-links {
  display: flex;
  gap: 2rem;
}

.nav-link {
  color: var(--yk-fontcolor);
  text-decoration: none;
  transition: color 0.3s;
}
.nav-link:hover {
  color: var(--yk-hovertext);
}

.login-btn {
  background-color: var(--yk-main);
  padding: 0.5rem 1rem;
  border-radius: 4px;
  transition: background-color 0.3s;
}
.login-btn:hover {
  background-color: var(--yk-main-op-deep);
  color: var(--yk-reverse);
}
</style>