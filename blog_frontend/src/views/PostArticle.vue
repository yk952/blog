<template>
  <div>
    <h1>发布文章</h1>
    <form>
      <label>标题：</label>
      <input type="text" name="title" required />
      <br />
      <label>内容：</label>
      <textarea name="content" rows="4" required></textarea>
      <br />
      <input type="submit" value="发布" />
    </form>
  </div>
</template>

<script setup lang="ts">

</script>
