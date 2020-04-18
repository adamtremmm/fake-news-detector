export class Tweet {
  public author: string;
  public text: string;
  public isTrue: boolean;

  constructor(author: string, text: string, isTrue: boolean) {
    this.author = author;
    this.text = text;
    this.isTrue = isTrue;
  }
}
