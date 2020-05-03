var app = new Vue({
  el: '#app',
  data: {
    title: 'vue-simple-upload'
  },
  components: {
    'fileupload': FileUpload.FileUpload
  }
})