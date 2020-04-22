import { Injectable } from '@angular/core';
import { Tweet } from '../models/tweet.model';
import { Subject } from 'rxjs';
import { HttpClient } from '@angular/common/http';
import { Router } from '@angular/router';

@Injectable({providedIn: 'root'})
export class TweetService {
  private tweet: Tweet;
  private tweets: Tweet[] = [];
  private tweetUpdated = new Subject<Tweet>();
  private tweetsUpdated = new Subject<Tweet[]>();

  constructor(
    private http: HttpClient,
    private router: Router
  ) {}

  postTweet(tweet: Tweet) {
    console.log('from tweet service');
    console.log(tweet);
    this.tweets.unshift(tweet);
    this.tweetsUpdated.next([...this.tweets]);
  }

  getTweets() {
    return [...this.tweets];
  }

  getTweetUpdateListener() {
    return this.tweetsUpdated.asObservable();
  }
}
