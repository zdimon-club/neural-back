


import { SnackbarService } from '../../../core/snackbar/snackbar.service';



private snackbarService: SnackbarService,

  // todo id should be id of chat room
  public showToast() {
    this.snackbarService.showToast({
      author: 'Nikola',
      message: 'Hello Bred how are yuo?',
      avatar: this.user.main_photo,
      id: '' + this.user.id
    });
  }