import { Component, OnInit } from '@angular/core';
import { Tweet } from '../models/tweet.model';
import { TweetService } from '../services/tweet.service';

@Component({
  selector: 'app-tweet',
  templateUrl: './tweet.component.html',
  styleUrls: ['./tweet.component.css']
})
export class TweetComponent implements OnInit {
  tweetService: TweetService;

  tweet: Tweet = {
    profilePic: './../../../assets/img/donald-trump.jpg',
    username: 'Donald J. Trump',
    handle: 'realDonaldTrump',
    timestamp: 'Just Now',
    text: '',
    isTrue: false
  };

  constructor(
    tweetService: TweetService
  ) {
    this.tweetService = tweetService;
  }

  ngOnInit(): void {
  }

  onClickTweetButton() {
    const newTweet = new Tweet(
      this.tweet.profilePic,
      this.tweet.username,
      this.tweet.handle,
      this.tweet.timestamp,
      this.tweet.text,
      this.tweet.isTrue
    );
    this.tweetService.postTweet(newTweet);
    this.tweet.text = '';
  }

}
