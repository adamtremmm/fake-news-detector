import { Component, OnInit } from '@angular/core';
import { Tweet } from "../tweet.model";

@Component({
  selector: 'app-tweet-list',
  templateUrl: './tweet-list.component.html',
  styleUrls: ['./tweet-list.component.css']
})
export class TweetListComponent implements OnInit {
  tweets: Tweet[] = [
    new Tweet("Donald J. Trump", "I am officially stepping down as President of the United States!", false)
  ];

  constructor() { }

  ngOnInit(): void {
  }

}
