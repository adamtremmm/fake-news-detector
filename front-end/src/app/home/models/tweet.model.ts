export class Tweet {
  public profilePic: string;
  public username: string;
  public handle: string;
  public timestamp: string;
  public text: string;
  public isTrue: string;

  constructor(
    profilePic: string,
    username: string,
    handle: string,
    timestamp: string,
    text: string,
    isTrue: string
  ) {
    this.profilePic = profilePic;
    this.username = username;
    this.handle = handle;
    this.timestamp = timestamp;
    this.text = text;
    this.isTrue = isTrue;
  }
}
