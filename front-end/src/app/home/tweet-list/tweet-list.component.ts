import { Component, OnInit, OnDestroy } from '@angular/core';
import { Tweet } from '../models/tweet.model';
import { TweetService } from '../services/tweet.service';
import { Subscription } from 'rxjs';

@Component({
  selector: 'app-tweet-list',
  templateUrl: './tweet-list.component.html',
  styleUrls: ['./tweet-list.component.css']
})
export class TweetListComponent implements OnInit, OnDestroy {
  tweets: Tweet[] = [];
  private tweetSub: Subscription;

  constructor(
    private tweetService: TweetService
  ) { }

  ngOnInit(): void {
    this.fetchPosts();
  }

  fetchPosts() {
    this.tweets = this.tweetService.getTweets();
    this.tweetSub = this.tweetService.getTweetUpdateListener()
      .subscribe((tweets: Tweet[]) => {
        this.tweets = tweets;
      });
  }

  ngOnDestroy() {
    this.tweetSub.unsubscribe();
  }
}
