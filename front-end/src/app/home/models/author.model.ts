export class AuthorModel {
  public profilePic: string;
  public username: string;
  public handle: string;

  constructor(
    profilePic: string,
    username: string,
    handle: string
  ) {
    this.profilePic = profilePic;
    this.username = username;
    this.handle = handle;
  }
}
