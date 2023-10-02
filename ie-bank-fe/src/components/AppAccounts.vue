<template>
  <div class="jumbotron vertical-center">
    <div class="container">
      <div class="row">
        <div class="col-sm-12">
          <h1>Accounts</h1>
          <hr />
          <br />
          <!-- Alert Message -->
          <b-alert v-if="showMessage" variant="success" show>{{ message }}</b-alert>

          <button
            type="button"
            class="btn btn-success btn-sm"
            v-b-modal.account-modal
          >
            Create Account
          </button>
          <br /><br />
          <table class="table table-hover">
            <thead>
              <tr>
                <th scope="col">Account Name</th>
                <th scope="col">Account Number</th>
                <th scope="col">Account Balance</th>
                <th scope="col">Account Currency</th>
                <th scope="col">Account Country</th> <!-- Added Country Column -->
                <th scope="col">Account Status</th>
                <th scope="col">Actions</th>
              </tr>
            </thead>
            <tbody>
              <tr v-for="account in accounts" :key="account.id">
                <td>{{ account.name }}</td>
                <td>{{ account.account_number }}</td>
                <td>{{ account.balance }}</td>
                <td>{{ account.currency }}</td>
                <td>{{ account.country }}</td> <!-- Display Country for each account -->
                <td>
                  <span
                    v-if="account.status == 'Active'"
                    class="badge badge-success"
                  >{{ account.status }}</span>
                  <span v-else class="badge badge-danger">{{ account.status }}</span>
                </td>
                <td>
                  <div class="btn-group" role="group">
                    <button
                      type="button"
                      class="btn btn-info btn-sm"
                      v-b-modal.edit-account-modal
                      @click="editAccount(account)"
                    >
                      Edit
                    </button>
                    <button
                      type="button"
                      class="btn btn-danger btn-sm"
                      @click="deleteAccount(account)"
                    >
                      Delete
                    </button>
                  </div>
                </td>
              </tr>
            </tbody>
          </table>
          <footer class="text-center">
            Copyright &copy; All Rights Reserved.
          </footer>
        </div>
      </div>
      <b-modal
        ref="addAccountModal"
        id="account-modal"
        title="Create a new account"
        hide-backdrop
        hide-footer
      >
        <b-form @submit="onSubmit" class="w-100">
          <b-form-group
            id="form-name-group"
            label="Account Name:"
            label-for="form-name-input"
          >
            <b-form-input
              id="form-name-input"
              type="text"
              v-model="createAccountForm.name"
              placeholder="Account Name"
              required
            ></b-form-input>
          </b-form-group>
          <b-form-group
            id="form-currency-group"
            label="Currency:"
            label-for="form-currency-input"
          >
            <b-form-input
              id="form-currency-input"
              type="text"
              v-model="createAccountForm.currency"
              placeholder="$ or €"
              required
            ></b-form-input>
          </b-form-group>
          <!-- Added Country Input Field -->
          <b-form-group
            id="form-country-group"
            label="Country:"
            label-for="form-country-input"
          >
            <b-form-input
              id="form-country-input"
              type="text"
              v-model="createAccountForm.country"
              placeholder="Country"
              required
            ></b-form-input>
          </b-form-group>
          <b-button type="submit" variant="outline-info">Submit</b-button>
        </b-form>
      </b-modal>
      <!-- End of Modal for Create Account-->
      <!-- Start of Modal for Edit Account-->
      <b-modal
        ref="editAccountModal"
        id="edit-account-modal"
        title="Edit the account"
        hide-backdrop
        hide-footer
      >
        <b-form @submit="onSubmitUpdate" class="w-100">
          <b-form-group
            id="form-edit-name-group"
            label="Account Name:"
            label-for="form-edit-name-input"
          >
            <b-form-input
              id="form-edit-name-input"
              type="text"
              v-model="editAccountForm.name"
              placeholder="Account Name"
              required
            ></b-form-input>
          </b-form-group>
          <b-button type="submit" variant="outline-info">Update</b-button>
        </b-form>
      </b-modal>
      <!-- End of Modal for Edit Account-->
    </div>
  </div>
</template>

<script>
import axios from "axios";
export default {
  name: "AppAccounts",
  data() {
    return {
      accounts: [],
      createAccountForm: {
        name: "",
        currency: "",
        country: ""  // Added Country Field
      },
      editAccountForm: {
        id: "",
        name: "",
      },
      showMessage: false,
      message: "",
    };
  },
  methods: {

onSubmit(e) {
  e.preventDefault();
  this.$refs.addAccountModal.hide();
  const payload = {
    name: this.createAccountForm.name,
    currency: this.createAccountForm.currency,
    country: this.createAccountForm.country
  };
  this.RESTcreateAccount(payload);
  this.initForm();
},

RESTcreateAccount(payload) {
    axios.post('/accounts', payload)
        .then(response => {
            this.accounts.push(response.data);
            this.showMessage = true;
            this.message = "Account created successfully!";
        })
        .catch(error => {
            console.error("Error creating account:", error);
            this.showMessage = true;
            this.message = "Error creating account!";
        });
},

onSubmitUpdate(e) {
    e.preventDefault();
    this.$refs.editAccountModal.hide();
    const payload = {
      name: this.editAccountForm.name,
    };
    this.RESTupdateAccount(payload, this.editAccountForm.id);
    this.initForm();
},

RESTupdateAccount(payload, id) {
    axios.put('/accounts/' + id, payload)
        .then(response => {
            // Update the account in the accounts array
            const index = this.accounts.findIndex(account => account.id === id);
            if (index !== -1) {
                this.accounts[index] = response.data;
            }
            this.showMessage = true;
            this.message = "Account updated successfully!";
        })
        .catch(error => {
            console.error("Error updating account:", error);
            this.showMessage = true;
            this.message = "Error updating account!";
        });
},

editAccount(account) {
    this.editAccountForm = account;
},

deleteAccount(account) {
    this.RESTdeleteAccount(account.id);
},

RESTdeleteAccount(id) {
    axios.delete('/accounts/' + id)
        .then(() => {
            const index = this.accounts.findIndex(account => account.id === id);
            if (index !== -1) {
                this.accounts.splice(index, 1);
            }
            this.showMessage = true;
            this.message = "Account deleted successfully!";
        })
        .catch(error => {
            console.error("Error deleting account:", error);
            this.showMessage = true;
            this.message = "Error deleting account!";
        });
},

RESTgetAccounts() {
    axios.get('/accounts')
        .then(response => {
            this.accounts = response.data.accounts;
        })
        .catch(error => {
            console.error("Error fetching accounts:", error);
            this.showMessage = true;
            this.message = "Error fetching accounts!";
        });
},

initForm() {
    this.createAccountForm.name = "";
    this.createAccountForm.currency = "";
    this.createAccountForm.country = "";
    this.editAccountForm.name = "";
}
},


  /***************************************************
   * LIFECYClE HOOKS
   ***************************************************/
  
  created() {
    this.RESTgetAccounts();
  },
};
</script>
