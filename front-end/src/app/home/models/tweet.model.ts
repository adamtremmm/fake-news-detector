export class Tweet {
  public profilePic: string;
  public username: string;
  public handle: string;
  public timestamp: string;
  public text: string;
  public isTrue: boolean;

  constructor(
    profilePic: string,
    username: string,
    handle: string,
    timestamp: string,
    text: string,
    isTrue: boolean
  ) {
    this.profilePic = profilePic;
    this.username = username;
    this.handle = handle;
    this.timestamp = timestamp;
    this.text = text;
    this.isTrue = isTrue;
  }
}
