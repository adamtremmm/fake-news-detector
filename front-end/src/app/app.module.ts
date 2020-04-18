import { BrowserModule } from '@angular/platform-browser';
import { NgModule } from '@angular/core';

import { AppComponent } from './app.component';
import { HeaderComponent } from "./header/header.component";
import { FormsModule } from "@angular/forms";
import { HomeComponent } from './home/home.component';
import { TweetListComponent } from './home/tweet-list/tweet-list.component';
import {TweetComponent} from "./home/tweet-list/tweet/tweet.component";

@NgModule({
  declarations: [
    AppComponent,
    HeaderComponent,
    HomeComponent,
    TweetListComponent,
    TweetComponent
  ],
  imports: [
    BrowserModule,
    FormsModule
  ],
  providers: [],
  bootstrap: [AppComponent]
})
export class AppModule { }
