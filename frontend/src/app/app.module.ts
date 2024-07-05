import { BrowserModule } from '@angular/platform-browser';
import { NgModule } from '@angular/core';
import { provideHttpClient } from '@angular/common/http';
import { ReactiveFormsModule } from '@angular/forms';

// Components
import { HomeComponent } from './home/home.component';

// Modules
import { AppRoutingModule } from './app-routing.module';
import { AppComponent } from './app.component';
import { WordleSolverComponent } from './wordle-solver/wordle-solver.component';

// Services


@NgModule({
	declarations: [AppComponent],
	imports: [
		AppRoutingModule,
		BrowserModule,
		ReactiveFormsModule,

		//components
		WordleSolverComponent,
		HomeComponent
	],
	providers: [provideHttpClient()],
	bootstrap: [AppComponent],
})
export class AppModule {}