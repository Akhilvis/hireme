
var app = new Vue({
  el: '#app',
  data: {
    title: 'vue-simple-upload'
  },
  components: {
    'fileupload': FileUpload.FileUpload
  }
})


new Vue({
    el: '#cand_form',

    data: {
        name: '',
        email: '',
        mobile: '',
        role: '',
        experience: ''
    },

    methods: {
        search: function(e) {
            e.preventDefault();

            $.post("/employee/add_candidate_data", {
                "name": this.name,
                "email": this.email,
                "mobile": this.mobile,
                "role": this.role,
                "experience": this.experience

                }, function(result){
                $("span").html(result);
              });

        }
    }
});