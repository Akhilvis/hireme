
var app = new Vue({
  el: '#upload_resume',
  data: {
    title: 'vue-simple-upload'
  },
  components: {
    'fileupload': FileUpload.FileUpload
  }
})


var app = new Vue({
  el: '#ftco-nav',
  data: {},
  methods: {
    scroll: function(div_id) {
             $('html, body').animate({
                scrollTop: $(div_id).offset().top
            }, 1000);
        }
        }
})



new Vue({
    el: '#cand_form',

    data: {
        name: '',
        email: '',
        mobile: '',
        role: '',
        experience: '',
        summary:'',
    },

    methods: {
        search: function(e) {
            e.preventDefault();

            $.post("/employee/add_candidate_data", {
                "name": this.name,
                "email": this.email,
                "mobile": this.mobile,
                "role": this.role,
                "experience": this.experience,
                "summary": this.summary

                }, function(result){
                $("span").html(result);
              });

        }
    }
});